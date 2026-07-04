Use the "l10n-sync" skill (read .agents/skills/l10n-sync/SKILL.md).

I want you to update @public/docs/ 
+ Thought: 66ms
→Skill "l10n-sync"
+ Thought: 728ms
Let me start by running the plan to see what needs syncing.
$ python3 -B /home/zorin/Documents/NPM/vistaz/.agents/skills/l10n-sync/scripts/l10n.py plan --source README.md --dir public/docs --work /tmp/l10n-work
{
  "targets": 11,
  "to_translate": [
    {
      "file": "public/docs/README_AR.md",
      "lang": "ar",
      "mode": "full",
      "blocks": 57
    },
    {
…
Click to expand
+ Thought: 677ms
11 languages × 57 blocks = 627 blocks total. This is a large job — I'll split the languages across parallel agents. Let me first read the jobs to understand what needs translating.
→Read /tmp/l10n-work/jobs.json 
+ Thought: 2.8s
I'll launch parallel agents — one per language — to translate all 57 blocks simultaneously.
# Todos
[•] Launch parallel translation agents for all 11 languages
[ ] Merge partial results
[ ] Apply translations to files
[ ] Verify all files pass checks
+ Thought: 506ms
✓General Task — Translate to Arabic
↳ 3 toolcalls · 28.1s
ctrl+x down view subagents
+ Thought: 186ms
✓General Task — Translate to German
↳ 3 toolcalls · 30.2s
ctrl+x down view subagents
+ Thought: 6ms
✓General Task — Translate to Spanish
↳ 3 toolcalls · 38.8s
ctrl+x down view subagents
+ Thought: 173ms
✓General Task — Translate to French
↳ 4 toolcalls · 1m 2s
ctrl+x down view subagents
+ Thought: 6ms
✓General Task — Translate to Hindi
↳ 4 toolcalls · 1m 30s
ctrl+x down view subagents
+ Thought: 23ms
✓General Task — Translate to Japanese
↳ 3 toolcalls · 33.9s
ctrl+x down view subagents
+ Thought: 385ms
✓General Task — Translate to Korean
↳ 3 toolcalls · 55.1s
ctrl+x down view subagents
+ Thought: 315ms
✓General Task — Translate to Portuguese
↳ 3 toolcalls · 23.1s
ctrl+x down view subagents
+ Thought: 829ms
│General Task — Translate to Russian
ctrl+x down view subagents
▣  Build · MiMo V2.5 Free ·