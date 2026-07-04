# Batching languages into one LLM call

To keep it to a single model round per sync *across all langs*, send one envelope:

```json
{
  "es": {"markdown:1": "Inicio", "markdown:3": "..."},
  "zh-cn": {"markdown:1": "主页", "markdown:3": "..."},
  "ja": {"markdown:1": "ホーム", "markdown:3": "..."}
}
```

Rules:
- Every language object MUST have the exact same key set as the payload template. Missing keys = the script flags the lang as incomplete and won't write its file.
- Languages you're less confident in can be left empty (`{}`) and the script will mark them `⚠ blanks` in the summary — do not write a partial `.md` for them. Re-run just those langs in a follow-up call.

Trade-off: one big call is ~11× the payload size of a single-lang call but saves 11 round trips. For a 130-line README the envelope is still under ~400 IDs × 11 langs ≈ 4,400 short strings — far smaller than 11 full-file rewrites.

If the model's context window is tight (or output token limit is hit mid-envelope), fall back to per-language calls in the order: es, fr, de, pt-br, it-adjacent first, then zh-cn, ja, ko, vi, hi, ar last (CJK and RTL are harder — give them isolated calls so they don't get squeezed by an earlier lang cutting off the output).

Print in chat which mode you used: "Batched all 11 langs in one call" or "Per-lang calls: es ✓ fr ✓ …".