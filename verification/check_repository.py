#!/usr/bin/env python3
"""Check repository navigation and the shared learning-map structure.

This is a structural checker. It does not verify scientific statements,
teaching quality, mathematical rendering, or the absence of every possible
personal detail. External links are not fetched.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit


def normalized_label(value):
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def heading_slug(value):
    value = html.unescape(re.sub(r"<[^>]*>", "", value))
    value = value.replace("`", "").replace("\\", "").lower()
    value = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", value)
    value = "".join(ch for ch in value if
                    ch in "_-" or ch.isspace() or
                    unicodedata.category(ch)[0] not in "PSC")
    return re.sub(r"\s", "-", value)


def strip_inline_code(line):
    """Remove code contents while preserving GitHub's $`math`$ form."""
    out=[]
    i=0
    while i<len(line):
        if line.startswith("$`",i):
            end=line.find("`$",i+2)
            if end<0:
                out.append(line[i:])
                break
            out.append(line[i:end+2])
            i=end+2
        elif line[i]=="`":
            run=len(line[i:])-len(line[i:].lstrip("`"))
            end=line.find("`"*run,i+run)
            if end<0:
                out.append(line[i:])
                break
            out.append(" "*(end+run-i))
            i=end+run
        else:
            out.append(line[i])
            i+=1
    return "".join(out)


def document_structure(path,text,errors):
    """Return text outside fences, headings and available GitHub-style IDs."""
    clean=[]
    headings=[]
    anchors=set()
    slug_counts=Counter()
    active_fence=None
    fence_start=None
    math_tokens=[]
    for number,line in enumerate(text.splitlines(),1):
        match=re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$",line)
        if active_fence is not None:
            if match and match.group(1)[0]==active_fence[0] and \
                    len(match.group(1))>=len(active_fence) and not match.group(2).strip():
                active_fence=None
            clean.append("")
            continue
        if match:
            active_fence=match.group(1)
            fence_start=number
            clean.append("")
            continue
        clean.append(line)
        h=re.match(r"^ {0,3}(#{1,6})\s+(.+?)\s*#*\s*$",line)
        if h:
            level=len(h.group(1))
            title=h.group(2)
            slug=heading_slug(title)
            count=slug_counts[slug]
            slug_counts[slug]+=1
            anchors.add(slug if count==0 else f"{slug}-{count}")
            headings.append({'line':number,'level':level,'title':title})
        anchors.update(re.findall(r"<a\b[^>]*\b(?:id|name)=[\"']([^\"']+)[\"']",line,re.I))
        line=strip_inline_code(line)
        i=0
        while i<len(line):
            if line[i]=="\\":
                if i+1<len(line) and line[i+1] in "()[]":
                    math_tokens.append((line[i:i+2],number))
                i+=2
                continue
            if line.startswith("$`",i):
                end=line.find("`$",i+2)
                if end<0:
                    errors.append(f"{path}:{number}: unclosed GitHub inline-math delimiter")
                    break
                i=end+2
                continue
            if line.startswith("$$",i):
                math_tokens.append(("$$",number));i+=2
            elif line[i]=="$":
                math_tokens.append(("$",number));i+=1
            else:
                i+=1
    if active_fence is not None:
        errors.append(f"{path}:{fence_start}: unclosed {active_fence} fence")
    stack=[]
    for token,number in math_tokens:
        if token in ("$","$$"):
            if stack and stack[-1][0]==token:
                stack.pop()
            elif stack:
                errors.append(f"{path}:{number}: nested or mismatched math delimiter {token}")
            else:
                stack.append((token,number))
        elif token in (r"\(",r"\["):
            stack.append((token,number))
        else:
            expected={r"\)":r"\(",r"\]":r"\["}[token]
            if not stack or stack[-1][0]!=expected:
                errors.append(f"{path}:{number}: unmatched math delimiter {token}")
            else:
                stack.pop()
    for token,number in stack:
        errors.append(f"{path}:{number}: unclosed math delimiter {token}")
    return {'clean':"\n".join(clean),'headings':headings,'anchors':anchors}


def markdown_links(text, inherited_definitions=None):
    """Read inline, reference-style and HTML link destinations outside fences."""
    found=[]
    definitions=dict(inherited_definitions or {})
    for number,line in enumerate(text.splitlines(),1):
        d=re.match(r"^ {0,3}\[([^\]]+)\]:\s*(\S+)",line)
        if d:
            destination=d.group(2).strip("<>")
            definitions[normalized_label(d.group(1))]=destination
            found.append((destination,number))
    for number,raw in enumerate(text.splitlines(),1):
        line=strip_inline_code(raw)
        i=0
        while True:
            start=line.find("](",i)
            if start<0:
                break
            cursor=start+2
            while cursor<len(line) and line[cursor].isspace():cursor+=1
            if cursor<len(line) and line[cursor]=="<":
                end=line.find(">",cursor+1)
                if end<0:break
                destination=line[cursor+1:end]
                i=end+1
            else:
                end=cursor
                depth=0
                while end<len(line):
                    if line[end]=="\\":end+=2;continue
                    if line[end]=="(":depth+=1
                    elif line[end]==")":
                        if depth==0:break
                        depth-=1
                    elif line[end].isspace() and depth==0:break
                    end+=1
                destination=line[cursor:end]
                i=max(end+1,cursor+1)
            if destination:found.append((destination,number))
        for match in re.finditer(r"\[([^\]]+)\]\[([^\]]*)\]",line):
            key=normalized_label(match.group(2) or match.group(1))
            if key in definitions:found.append((definitions[key],number))
        for match in re.finditer(r"(?<!!)\[([^\[\]]+)\](?![\[(])",line):
            key=normalized_label(match.group(1))
            if key in definitions:found.append((definitions[key],number))
        for match in re.finditer(r"<(?:a|img)\b[^>]*\b(?:href|src)=[\"']([^\"']+)[\"']",line,re.I):
            found.append((html.unescape(match.group(1)),number))
    return found


def check_navigation(root,documents,structures,errors):
    relative_count=0
    anchor_count=0
    external_count=0
    graph={rel:set() for rel in documents}
    for rel,structure in structures.items():
        for target,line in markdown_links(structure['clean']):
            parsed=urlsplit(target)
            if parsed.scheme or parsed.netloc:
                external_count+=1
                continue
            if target.startswith("/"):
                errors.append(f"{rel}:{line}: root-relative destination is not repository-relative: {target}")
                continue
            relative_count+=1
            destination=((root/rel).parent/unquote(parsed.path)).resolve() if parsed.path else root/rel
            try:
                dest_rel=destination.relative_to(root).as_posix()
            except ValueError:
                errors.append(f"{rel}:{line}: relative target escapes repository: {target}")
                continue
            if not destination.exists():
                errors.append(f"{rel}:{line}: missing relative target: {target}")
                continue
            graph_target=destination/'README.md' if destination.is_dir() else destination
            graph_rel=graph_target.relative_to(root).as_posix()
            if graph_rel in documents:graph[rel].add(graph_rel)
            if parsed.fragment:
                anchor_count+=1
                if destination.is_dir():
                    destination=destination/'README.md'
                    dest_rel=destination.relative_to(root).as_posix()
                if destination.suffix.lower() in ('.md','.markdown'):
                    if dest_rel not in structures:
                        errors.append(f"{rel}:{line}: unreadable Markdown anchor target: {target}")
                    elif unquote(parsed.fragment) not in structures[dest_rel]['anchors']:
                        errors.append(f"{rel}:{line}: missing target anchor: {target}")
                else:
                    errors.append(f"{rel}:{line}: fragment on non-Markdown target cannot be structurally checked: {target}")
    reachable=set()
    pending=['README.md'] if 'README.md' in documents else []
    while pending:
        current=pending.pop()
        if current in reachable:continue
        reachable.add(current)
        pending.extend(graph[current]-reachable)
    orphaned=sorted(set(documents)-reachable)
    for rel in orphaned:errors.append(f"{rel}: Markdown page is not reachable from README.md through relative links")
    llms=root/'llms.txt'
    llms_targets=[]
    if llms.exists():
        llms_targets=sorted(set(re.findall(r'(?<![A-Za-z0-9_./-])([A-Za-z0-9_./-]+\.(?:md|txt|bib|py|json|cjs|yml))\b',llms.read_text())))
        for target in llms_targets:
            if not (root/target).exists():errors.append(f"llms.txt: missing local reading-guide target {target}")
    return {'relative_destinations_checked':relative_count,
            'relative_fragments_checked':anchor_count,
            'external_destinations_not_fetched':external_count,
            'markdown_pages_reachable_from_readme':len(reachable),
            'orphaned_markdown_pages':orphaned,
            'local_llms_guide_targets_checked':llms_targets}


def read_fields(body):
    fields={}
    current=None
    for line in body.splitlines():
        match=re.match(r"^\s*\*\*([^*]+)\*\*\s*:?[ \t]*(.*)$",line)
        if match:
            current=normalized_label(match.group(1).rstrip(':'))
            fields[current]=match.group(2)
        elif current is not None:
            fields[current]+="\n"+line
    return fields


def check_milestones(root,documents,structures,errors):
    rel='learning/MILESTONES.md'
    if rel not in documents:
        errors.append(f"{rel}: required shared milestone map is missing")
        return {}
    lines=documents[rel].splitlines()
    milestones=[]
    phases=[]
    current_phase=None
    for heading in structures[rel]['headings']:
        title=heading['title']
        marker=re.match(r"M(\d{2})\b",title)
        if marker:
            milestones.append({**heading,'id':int(marker.group(1)),'phase':current_phase})
        elif heading['level']==2 and re.search(r"background|preliminar|narrative|innovation",title,re.I):
            current_phase=len(phases)
            phases.append({**heading,'ids':[]})
    ids=[x['id'] for x in milestones]
    if ids!=list(range(1,31)):
        errors.append(f"{rel}: milestone headings must contain M01 through M30 exactly once and in order; found {ids}")
    required=['phase','central question','understanding target','dependencies and story role',
              'conceptual connection','source pointers']
    source_definitions={normalized_label(m.group(1)):m.group(2).strip('<>')
                        for m in re.finditer(r'^ {0,3}\[([^\]]+)\]:\s*(\S+)',documents[rel],re.M)}
    graph={}
    for index,item in enumerate(milestones):
        end=milestones[index+1]['line']-1 if index+1<len(milestones) else len(lines)
        # A phase heading belongs to its following milestone, not the prior one.
        for phase in phases:
            if item['line']<phase['line']<=end:end=phase['line']-1
        body="\n".join(lines[item['line']:end])
        fields=read_fields(body)
        mid=item['id']
        for key in required:
            if not fields.get(key,'').strip():
                errors.append(f"{rel}:{item['line']}: M{mid:02d} lacks nonempty field '{key}'")
        dependencies=sorted(set(map(int,re.findall(r"\bM(\d{2})\b",fields.get('dependencies and story role','')))))
        graph[mid]=dependencies
        for dependency in dependencies:
            if dependency<1 or dependency>=mid:
                errors.append(f"{rel}:{item['line']}: M{mid:02d} dependency M{dependency:02d} is not an earlier milestone")
        if mid>1 and not dependencies:
            errors.append(f"{rel}:{item['line']}: M{mid:02d} declares no earlier milestone dependency")
        if not markdown_links(fields.get('source pointers',''),source_definitions):
            errors.append(f"{rel}:{item['line']}: M{mid:02d} has no linked source pointer")
        if item['phase'] is None:
            errors.append(f"{rel}:{item['line']}: M{mid:02d} is outside the two phase sections")
        else:
            phase=phases[item['phase']]
            phase['ids'].append(mid)
            declared=normalized_label(fields.get('phase',''))
            expected='background preliminaries' if re.search(r'background|preliminar',phase['title'],re.I) else 'narrative innovation'
            if not all(word in declared for word in expected.split()):
                errors.append(f"{rel}:{item['line']}: M{mid:02d} phase field disagrees with its section")
    if len(phases)!=2:
        errors.append(f"{rel}: expected two declared phases; found {len(phases)}")
    for phase in phases:
        if not phase['ids']:
            errors.append(f"{rel}:{phase['line']}: empty phase")
        match=re.search(r"M(\d{2})\s*[–—-]\s*M(\d{2})",phase['title'])
        if match and phase['ids']!=list(range(int(match.group(1)),int(match.group(2))+1)):
            errors.append(f"{rel}:{phase['line']}: declared phase range disagrees with contained milestones")
    # Earlier-ID dependency validation above implies a DAG; retain an explicit
    # graph traversal so future schema changes cannot silently remove that check.
    active=set();finished=set()
    def visit(node):
        if node in active:
            errors.append(f"{rel}: dependency cycle through M{node:02d}")
            return
        if node in finished:return
        active.add(node)
        for parent in graph.get(node,[]):visit(parent)
        active.remove(node);finished.add(node)
    for node in graph:visit(node)
    return {'ids':[f'M{x:02d}' for x in ids],
            'phase_partition':[{'heading':p['title'],'count':len(p['ids']),
                                'ids':[f'M{x:02d}' for x in p['ids']]} for p in phases],
            'dependency_edges':sum(map(len,graph.values())),
            'dependency_graph':{f'M{k:02d}':[f'M{x:02d}' for x in v] for k,v in graph.items()},
            'required_fields':required}


def check_anchor_and_public_structure(root,documents,errors):
    declarations={}
    for rel in ['learning/README.md','learning/WATROUS_BRIDGE.md']:
        text=documents.get(rel,'')
        source_lines=[line for line in text.splitlines()
                      if re.search(r'educational anchor\s+(?:is|:)',line,re.I)]
        good=bool(source_lines) and all(
            re.search(r'Watrous',line,re.I) and
            re.search(r'The Theory of Quantum Information',line,re.I) and
            re.search(r'\b2018\b',line) for line in source_lines)
        declarations[rel]=good
        if not good:errors.append(f"{rel}: selected Watrous 2018 source identity is missing")
    forbidden_directories={'private','coaching','portfolio','checkpoints'}
    for path in root.iterdir():
        if path.is_dir() and path.name.lower() in forbidden_directories:
            errors.append(f"{path.name}/: personal or process directory is present in the scientific repository")
    patterns=[r'\b(?:Merlin|Arthur|Guinevere|Camelot)\b',
              r'\bportfolio\s+(?:ranking|shortlist|score)\b',
              r'\bpersonal\s+(?:coaching|assessment|progress)\b',
              r'^\s*#{1,6}\s+.*\b(?:learner state|coaching guide|assessment history)\b']
    markers=[]
    for rel,text in documents.items():
        if re.search(r'(^|/)(?:COACHING|CHECKPOINT)(?:\.|/|$)',rel,re.I):
            errors.append(f"{rel}: personal or process record filename")
        for number,line in enumerate(text.splitlines(),1):
            if any(re.search(pattern,line,re.I) for pattern in patterns):
                markers.append({'path':rel,'line':number})
                errors.append(f"{rel}:{number}: personal/process marker requires review")
    return {'selected_source':'John Watrous, The Theory of Quantum Information (2018)',
            'source_identity_presence':declarations,
            'public_marker_matches':markers,
            'scope':'Textual source-identity checks and narrow personal/process markers; manual source and content review remain necessary.'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output',type=Path,help='Optional JSON report destination')
    args=parser.parse_args()
    root=args.root.resolve()
    documents={p.relative_to(root).as_posix():p.read_text() for p in sorted(root.rglob('*.md'))
               if '.git' not in p.relative_to(root).parts}
    errors=[]
    structures={rel:document_structure(rel,text,errors) for rel,text in documents.items()}
    result={'status':'passed','scope':'Structural navigation, delimiter and learning-map checks only; no scientific, semantic, visual or external-link certification.',
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'markdown_files_checked':len(documents),
            'markdown_file_sha256':{rel:hashlib.sha256(text.encode()).hexdigest() for rel,text in documents.items()},
            'navigation':check_navigation(root,documents,structures,errors),
            'milestones':check_milestones(root,documents,structures,errors),
            'anchor_and_public_structure':check_anchor_and_public_structure(root,documents,errors),
            'errors':errors}
    if errors:result['status']='failed'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(f"{result['status'].upper()}: {len(documents)} Markdown files; "
          f"{result['navigation']['relative_destinations_checked']} relative destinations; "
          f"{len(result['milestones'].get('ids',[]))} milestones")
    for error in errors:print('ERROR:',error)
    if args.output:print('Results:',args.output)
    raise SystemExit(bool(errors))


if __name__=='__main__':main()
