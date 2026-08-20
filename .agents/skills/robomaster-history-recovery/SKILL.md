---
name: robomaster-history-recovery
description: Recover useful RoboMaster evidence, tables, figures, or research that appears lost in prior Git revisions. Use only for a defined missing topic, not routine chapter editing.
---

# Targeted history recovery

Define the missing chapter/topic, distinctive phrase, table/figure/source, or likely commit before searching.

1. Search the working tree and current research indexes first.
2. Use targeted `git log --all -- <path>`, `git log -S<phrase>`, `git log -G<pattern>`, and `git show <commit>:<path>` as appropriate.
3. Inspect only commits and paths that match the target; do not read every historical revision or treat one snapshot as the baseline.
4. Extract evidence, source identity, media references, or useful structure. Do not restore old prose blindly.
5. Recheck recovered claims against current rules, `dic.md`, live source availability, and `research/china-2026/claims-audit.md`. Never restore unsupported or superseded claims.
6. Record the recovered topic or unresolved absence in the relevant `REPORT_PLAN.md` evidence-map entry or `REVISION_STATUS.md` issue field.

Do not commit, reset, checkout over user work, or push without explicit instruction.
