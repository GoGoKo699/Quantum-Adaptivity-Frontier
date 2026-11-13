#!/usr/bin/env python3
"""Reproduce finite diagnostics for adaptive-trit exclusion and simulation bounds.

The written proofs establish the universal results. These calculations test
normalizations, constructions, finite minimax values, and scalar inequalities.
"""
import argparse
import hashlib
import itertools
import json
import math
import platform
from fractions import Fraction
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import qr
from scipy.optimize import linprog
from scipy.special import gammaln


def require(condition, message="Scientific check failed"):
    if not condition:
        raise AssertionError(message)


def haar(r, rng):
    z = (rng.normal(size=(r,r)) + 1j*rng.normal(size=(r,r)))/math.sqrt(2)
    q, a = qr(z, mode='economic')
    return q*(np.diag(a)/np.abs(np.diag(a)))


def global_small_support_check():
    r = 512
    rng = np.random.default_rng(812)
    bases = [np.eye(r, dtype=complex), haar(r,rng), haar(r,rng)]
    maxima = []
    for a,b in itertools.combinations(range(3),2):
        weights = np.abs(bases[a].conj().T@bases[b])**2
        # Every nonempty p-by-q submatrix with p+q<=3 is 1x1,
        # 1x2 or 2x1. These top-two masses give their exact global max.
        value = math.sqrt(max(
            np.partition(weights,-2,axis=0)[-2:,:].sum(axis=0).max(),
            np.partition(weights,-2,axis=1)[:,-2:].sum(axis=1).max()))
        maxima.append(float(value))
    require(max(maxima)<0.25)

    results = []
    max_complete = 0.0
    max_exclusion = 0.0
    min_eigen_a = math.inf
    min_eigen_c = math.inf
    min_eigen_g = math.inf
    max_probability_normalization = 0.0
    # Every composition of m=3 into three blocks, including empty blocks.
    for sizes in ((p,q,3-p-q) for p in range(4) for q in range(4-p)):
        for trial in range(5):
            selected = [rng.choice(r,s,replace=False) for s in sizes]
            vs = [u[:,ids] for u,ids in zip(bases,selected)]
            t = np.concatenate(vs,axis=1)
            g = t.conj().T@t
            g_inv = np.linalg.inv(g)
            q_span,_ = qr(t,mode='economic')
            h = q_span.conj().T@t
            offsets = np.cumsum((0,)+sizes)
            cs=[]
            for omitted in range(3):
                c=g.copy()
                for a in range(3):
                    sl=slice(offsets[a],offsets[a+1])
                    c[sl,sl]=0.5*np.eye(sizes[a])
                sl=slice(offsets[omitted],offsets[omitted+1])
                c[sl,:]=0
                c[:,sl]=0
                cs.append(c)
            aa=[h@g_inv@c@g_inv@h.conj().T for c in cs]
            complete=np.linalg.norm(sum(aa)-np.eye(3),ord=2)
            max_complete=max(max_complete,float(complete))
            min_eigen_g=min(min_eigen_g,float(np.linalg.eigvalsh(g).min()))
            min_eigen_c=min(min_eigen_c,*[float(np.linalg.eigvalsh(c).min()) for c in cs])
            min_eigen_a=min(min_eigen_a,*[float(np.linalg.eigvalsh(a).min()) for a in aa])
            for a,ids in enumerate(selected):
                for j in ids:
                    coeff=q_span.conj().T@bases[a][:,j]
                    prob=(coeff.conj()@aa[a]@coeff).real/r
                    max_exclusion=max(max_exclusion,abs(float(prob)))
            # Independent all-output probabilities from full-space A on one
            # representative of every split; trace(A)/r must sum to one.
            probs=[]
            for a,u in enumerate(bases):
                z=q_span.conj().T@u
                outside=1-np.sum(np.abs(z)**2,axis=0)
                p=(np.einsum('ij,ij->j',z.conj(),aa[a]@z).real+outside/3)/r
                require(p.min()>-1e-12)
                probs.extend(p.tolist())
            max_probability_normalization=max(max_probability_normalization,abs(sum(probs)-1))
            results.append({'sizes':sizes,'trial':trial})
    require(max_complete<1e-11)
    require(min_eigen_g>=0.5-1e-11)
    require(min_eigen_a>-1e-11 and min_eigen_c>-1e-11)
    require(max_exclusion<1e-12)
    require(max_probability_normalization<1e-11)
    return {
        'dimension':r,'excluded_set_size':3,'seed':812,
        'global_cross_submatrix_maxima':maxima,
        'all_cross_supports_with_total_size_at_most_3_checked':True,
        'povm_samples':len(results),'all_10_support_splits_sampled':True,
        'minimum_gram_eigenvalue':min_eigen_g,
        'minimum_split_matrix_eigenvalue':min_eigen_c,
        'minimum_reduced_povm_eigenvalue':min_eigen_a,
        'maximum_completeness_operator_residual':max_complete,
        'maximum_forbidden_event_probability':max_exclusion,
        'maximum_all_output_normalization_error':max_probability_normalization,
        'scope':'Full cross-submatrix support sweep at m=3; 50 sampled complete POVMs, not every excluded set.'
    }


def explicit_bipartite_check():
    r=16
    rng=np.random.default_rng(22)
    bases=[np.eye(r,dtype=complex),haar(r,rng),haar(r,rng)]
    sizes=(1,1,1)
    ids=[[0],[1],[2]]
    vs=[u[:,j] for u,j in zip(bases,ids)]
    t=np.concatenate(vs,axis=1)
    g=t.conj().T@t
    inv=np.linalg.inv(g)
    p=t@inv@t.conj().T
    aa=[]
    for omitted in range(3):
        c=g.copy();np.fill_diagonal(c,0.5)
        c[omitted,:]=0;c[:,omitted]=0
        require(np.linalg.eigvalsh(c).min()>-1e-12)
        aa.append(t@inv@c@inv@t.conj().T+(np.eye(r)-p)/3)
    phi=np.eye(r).reshape(-1)/math.sqrt(r)
    max_diff=0.0;forbidden=[];total=0.0
    for a in range(3):
        for j in range(r):
            u=bases[a][:,j]
            b=np.outer(u,u.conj())
            direct=(phi.conj()@np.kron(aa[a].T,b)@phi).real
            born=(u.conj()@aa[a]@u).real/r
            max_diff=max(max_diff,abs(float(direct-born)))
            total+=direct
            if j==ids[a][0]:forbidden.append(float(direct))
    require(max_diff<1e-12 and abs(total-1)<1e-12)
    require(max(map(abs,forbidden))<1e-12)
    return {'dimension':r,'sizes':sizes,'selected_indices':ids,
            'maximum_explicit_tensor_vs_born_probability_error':max_diff,
            'forbidden_probabilities':forbidden,'total_probability':float(total),
            'scope':'All 48 outputs of one valid 16-dimensional three-block POVM; actual tensor-product trace.'}


def classical_check():
    rows=[];max_lp_error=0.0;max_uniform_error=0.0
    for n in range(3,9):
        for m in range(1,n):
            subsets=list(map(frozenset,itertools.combinations(range(n),m)))
            for k in range(1,min(m+1,n)+1):
                lists=list(map(frozenset,itertools.combinations(range(n),k)))
                failures=np.array([[float(b.issubset(s)) for b in lists] for s in subsets])
                exact=math.comb(m,k)/math.comb(n,k) if k<=m else 0.0
                uniform=failures.mean(axis=1)
                max_uniform_error=max(max_uniform_error,float(np.max(np.abs(uniform-exact))))
                objective=np.r_[np.zeros(len(lists)),1.0]
                sol=linprog(objective,A_ub=np.c_[failures,-np.ones(len(subsets))],
                            b_ub=np.zeros(len(subsets)),A_eq=np.array([np.r_[np.ones(len(lists)),0]]),
                            b_eq=[1],bounds=[(0,None)]*(len(lists)+1),method='highs')
                require(sol.success)
                max_lp_error=max(max_lp_error,abs(float(sol.fun-exact)))
                rows.append({'n':n,'m':m,'k':k,'exact_error':exact,'lp_error':float(sol.fun)})
    require(max_lp_error<1e-10 and max_uniform_error<1e-12)
    return {'instances':len(rows),'n_range':[3,8],
            'maximum_lp_vs_binomial_error':max_lp_error,
            'maximum_uniform_strategy_vs_binomial_error':max_uniform_error,
            'details':rows,
            'scope':'All k-element deterministic output sets; smaller lists can be padded, so they cannot improve minimax error.'}


def union_bound_check():
    beta=math.log(247/256)
    alpha=(math.log(2048*math.e)+2*math.log(17))/1024+beta
    intercept=math.log(3)-beta
    at_start=intercept+1024*alpha
    require(alpha<0 and at_start<0)
    diagnostics=[]
    for r in [1024,1025,2047,2048,4096,10000,1000000]:
        m=r//1024
        log_exact=math.log(3)+gammaln(2*r+1)-gammaln(m+1)-gammaln(2*r-m+1)+2*m*math.log(17)+(r-1)*beta
        log_envelope=intercept+r*alpha
        require(log_exact<=log_envelope+1e-7 and log_envelope<0)
        diagnostics.append({'R':r,'m':m,'log_union_bound':float(log_exact),'log_linear_envelope':log_envelope})
    return {'c':1/1024,'net_radius':1/8,'net_cardinality_factor':17,
            'scalar_tail_threshold':3/16,'scalar_tail_base':247/256,
            'linear_envelope_slope':alpha,'linear_envelope_intercept':intercept,
            'envelope_at_R1024':at_start,
            'analytic_argument':'For x=m/R<=1/1024, x ln(2e/x)+2x ln17 is increasing. Thus log failure <= ln3-ln(247/256)+R[(ln(2048e)+2ln17)/1024+ln(247/256)]. Its slope and value at R=1024 are negative.',
            'diagnostics':diagnostics,
            'scope':'Analytical scalar bound plus floating diagnostics; no random-basis theorem is certified by sampling.'}


def integer_frontier_check():
    """Exact-rational diagnostics; game error is not correlation TV distance."""
    rows=[]
    for r in [2048,4096,8192,65536]:
        m=r//1024
        for power in [3,10,50]:
            epsilon=Fraction(1,10**power)
            # Exact minimax number of symbols for the exclusion game alone.
            game_minimum=next(k for k in range(1,m+2)
                              if (Fraction(math.comb(m,k),math.comb(3*r,k))
                                  if k<=m else Fraction(0))<=epsilon)
            # Inherited guessing simulation: N trials, plus one all-fail label.
            trials=0
            failure=Fraction(1)
            while failure>epsilon:
                trials+=1
                failure*=Fraction(2,3)
            universal_upper=min(3*r,trials+1)
            precision_lower=1
            elementary_failure=Fraction(1,12288)
            while elementary_failure>epsilon:
                precision_lower+=1
                elementary_failure/=12288
            elementary_lower=min(m//2+1,precision_lower)
            require(elementary_lower<=game_minimum<=universal_upper)
            for k in range(1,m//2+1):
                ratio=Fraction(math.comb(m,k),math.comb(3*r,k))
                require(ratio>=Fraction(1,12288)**k)
            rows.append({'R':r,'m':m,'epsilon':f'1e-{power}',
                         'elementary_simulation_alphabet_lower_bound':elementary_lower,
                         'exact_exclusion_game_alphabet':game_minimum,
                         'inherited_correlation_simulation_alphabet_upper_bound':universal_upper})
    return {'instances':len(rows),'arithmetic':'Exact Python integers and Fraction',
            'details':rows,
            'scope':'The exact game alphabet supplies a correlation-simulation lower bound. The game-optimal protocol is not asserted to reproduce the full quantum correlation.'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,
                        default=Path(__file__).resolve().parent/'results'/'science_checks.json',
                        help='Path for the complete JSON report')
    args=parser.parse_args()
    result={'status':'passed',
            'provenance':{'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                          'python_version':platform.python_version(),
                          'numpy_version':np.__version__,
                          'scipy_version':scipy.__version__,
                          'haar_seed':812,'explicit_tensor_seed':22},
            'global_support_and_povm':global_small_support_check(),
            'independent_tensor_probability':explicit_bipartite_check(),
            'classical_minimax':classical_check(),
            'universal_union_bound':union_bound_check(),
            'integer_frontier':integer_frontier_check()}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: all scientific finite checks')
    print(f"POVM samples: {result['global_support_and_povm']['povm_samples']}; "
          f"classical LP instances: {result['classical_minimax']['instances']}; "
          f"integer frontier diagnostics: {result['integer_frontier']['instances']}")
    print(f"Results: {args.output}")


if __name__=='__main__':main()
