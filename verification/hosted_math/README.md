# Check the hosted mathematics

The [workflow](../../.github/workflows/hosted-math.yml) checks mathematical expressions in the exact proposed source commit against their actual rendering on GitHub. It opens public commit-pinned pages in a fresh anonymous Chromium context at widths of 1440 and 760 pixels. The final comparison covers every tracked Markdown page, including the scientific account, learning material, references, and verification guides.

The comparison retains subscripts, superscripts, fractions, matrix structure, relations and labels. Missing expressions, renderer errors, structural differences and suspicious display geometry fail. Its artifact contains the source inventory, actual accessible mathematical content, screenshots, comparison results and a report with file hashes. The commit and tree identify precisely what was checked.

## Representative diagnostic

With a compatible runtime, inspect one actual page at both widths before the full review:

```bash
node verification/hosted_math/probe_hosted_math.cjs \
  --root /absolute/repository \
  --repository GoGoKo699/Quantum-Adaptivity-Frontier \
  --revision FULL_COMMIT_SHA --page README.md \
  --output /absolute/new-diagnostic-directory
```

Replace the illustrative paths and revision with actual values. A representative pass is an early diagnostic and does not establish full repository readiness.

## Complete source-bound comparison

Use Node.js 18 or later, Python 3.10 or later, Git, Playwright and MathJax. Install browser dependencies outside the repository:

```bash
npm install --prefix /absolute/runtime playwright@1.56.1 mathjax-full@3.2.1
/absolute/runtime/node_modules/.bin/playwright install chromium
NODE_PATH=/absolute/runtime/node_modules node verification/hosted_math/capture_hosted_math.cjs \
  --root /absolute/repository \
  --repository GoGoKo699/Quantum-Adaptivity-Frontier \
  --revision FULL_COMMIT_SHA \
  --output /absolute/new-capture-directory
```

The source inventory reads exact Git objects at that commit, ignoring uncommitted edits. Each attempt uses a new directory so failures remain inspectable. A transiently interrupted capture can explicitly resume eligible exact-source receipts into another new directory using `--resume-from /absolute/previous-directory`; changed source, tools or stale observations cannot be silently reused.

## Interpretation and access

A passing automated comparison still requires visual inspection of the screenshots against the source, including proof displays, tables and the learning route. It does not certify scientific correctness, literature priority or future renderer behavior. Local mathematical compilation is only the reference side of this comparison, not evidence that GitHub displayed the page correctly.

The CI job uses `contents: read`, has no secret input, checks out the exact same-repository pull-request head without persisted credentials, and leaves its browser unsigned in. Its artifacts expire after 14 days; that retention is not a permanent archive. The verifier scripts are versioned with the scientific source so their exact implementation and reports can be reproduced.

[Finite and learning checks](../README.md) · [Repository overview](../../README.md)
