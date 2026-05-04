# LeadHuman.ai Blog: AI-Voice Audit — 2026-05-04

## Why this audit exists

Following the 2026-05-03 Peak Potential blog scrub, Jay flagged that the same family of AI tells almost certainly affects the LeadHuman.ai corpus. The LH cloud drafter was written in the same style as the PP one and likely had the same internal contradictions PP did (mandating formulaic structure while forbidding "AI tells"). The PP smoking gun was that the cloud trigger itself mandated the tells via examples. This audit confirms the same root cause for LH and ships matching fixes.

**Bottom line:** the LH corpus is less lexically AI-flavored than PP was (better existing voice rules, fewer repeated banned phrases), but it shows high *structural* predictability. 9 of 16 posts close with a "X Things to Try" numbered action list; 100% of posts follow the same research-citation-then-anecdote sandwich; 100% close with the same template. The root cause is that the Monday and Thursday cloud triggers each contain a frozen inline prompt that mandates a fixed multi-section template and contains the banned phrase 'Hidden cause' as an explicit section name.

## Smoking-gun findings

### Monday /lead/ trigger (`trig_01G4wG4UhoH1kjybdoZkuUCp`)

The original prompt:
- **Mandated 'Hidden cause'** as a section heading: Step 4.2 read literally `"Diagnosis (1-2 paragraphs): Hidden cause. WHY before the fix."` That phrase is on the banned list across the rest of the rule set.
- **Mandated a fixed 9-section template** in exact order: Hook → Diagnosis → Research citation → Callout block → Actionable section → Conversational close → Genuine question → LinkedIn CTA → Sources. Same root cause as the PP "12-section canonical template" issue.
- **Hardcoded leaked Telegram bot token** in the curl call (`bot8771669297:AAEQCDxM745GDTsqrKgDM_WIjgfW80jtBNE`, the same token that was leaked in the PP trigger).
- Generic "Anti-AI" rules naming `delve`, `landscape`, `navigate`, `comprehensive`, `robust`, `Furthermore`, `Moreover`, but ZERO bans on the 18 confirmed Claude tells from the 2026 external research (em-dash cascades, contrastive negation, "Here's the thing", "honest answer", etc.).
- **Anti-self-plagiarism logic existed but was title-only**. Gates 1–5 in the executable bash block checked title patterns and pillar rotation, but the body opening overlap check looked at only the last 2 posts and there was no section-header-copy check or banned-phrase grep gate.

### Thursday /build/ trigger (`trig_01FmF5MK27E6mCHCGVZKFbTT`)

The original prompt:
- **Mandated a fixed 8-section tutorial template** in exact order: Hook → What you'll build → Why this matters → The build → Real example output → Where this breaks → What to do next → LinkedIn CTA. Same rigidity issue.
- **Same hardcoded leaked Telegram bot token.**
- **Generic Anti-AI** with NO tutorial-specific tell guards. The 2026 external research flagged step bloat, recap sections, "Let's dive into" / "In this tutorial we will" signposting, and "robust / scalable / enterprise-grade" adjective inflation as tutorial-class fingerprints. The original prompt addressed none of these.
- **No anti-self-plagiarism logic at all** for /build/. No title uniqueness gate, no opening overlap check, no executable bash gate, no banned-phrase grep.

Both prompts were internally contradictory. The structural mandates produced the formulaic output the anti-AI rules tried to forbid. The local files (`SKILL.md`, `CLAUDE.md`) are NOT consulted by the cloud triggers at runtime; the cloud triggers carry their own frozen copies of the rules. Same pattern as PP.

## Quantitative findings (corpus = 16 EN posts, 14 in /lead/, 2 in /build/, plus 10 JP versions)

### Cross-post repeated formulaic patterns

| Pattern | Posts containing | Status |
|---------|------------------|--------|
| "X Things to Try" / "Four Things to Try" / numbered action-list close | **9 / 16** | Mandated by trigger structural template |
| Research-citation-then-anecdote sandwich structure | **16 / 16** | Mandated by trigger Step 4 |
| Identical closing-paragraph template (research → bridge → CTA → newsletter push) | **15 / 16** | Mandated by trigger Step 4 |
| "isn't the [problem/barrier]. It's the [Y]" negation-reframe | 4 / 16 | Cadence effect |
| "The ones who [verb]" opener pattern | 4+ instances | Voice marker effect |
| "Here's what I keep seeing" / "Here's what I see" opener | 3+ instances | Voice marker effect |
| "And [substantial statement]" sentence-start | 15+ instances corpus-wide | Conversational tic, but heavy |

### Banned-phrase counts (LH corpus snapshot before scrub)

LH has lower lexical density of the PP-banned phrases than PP did:

| Phrase | Posts containing | Total occurrences |
|--------|------------------|--------------------|
| "Something I see constantly" / variants | 1 / 16 | 1 |
| "I'd argue" | 0 / 16 | 0 |
| "honest answer" / "honest truth" | 1 / 16 | 1 |
| "uncomfortable" (in voice context) | 4 / 16 | 4 |
| "What tends to happen" | 0 / 16 | 0 |
| "deceptively" | 0 / 16 | 0 |
| "the hidden cause" | 0 / 16 | 0 |
| "A lingering thought" | 0 / 16 | 0 |
| "Two managers at the same company" | 0 / 16 | 0 |

Existing local voice rules (in `CLAUDE.md` and `SKILL.md`) had already filtered out most of these vocabulary-level tells. The structural and cadence tells slipped through because the cloud trigger prompt actively mandated them.

### Em-dashes

| Hub | Mean per post | Range |
|-----|----------------|-------|
| /lead/ | 1.9 | 0–5 |
| /build/ | 4.0 | 2–6 |

Top em-dash offenders: `words-you-cant-translate` (5), `ai-changing-ld` (4), `why-leaders-need-ai` (4), `why-your-proposal-died` (4). 5 posts had zero em-dashes. The hyphen ban was already in place; the leakage came from typed em-dashes in body prose.

### Top 5 highest-tell-density posts (priority rewrites)

Ranked by combined em-dash + banned-phrase + formulaic-structure count:

1. `why-leaders-need-ai` — 7 tells (1 X-things, 1 "the real", 4 em-dashes, 1 "And"-start)
2. `words-you-cant-translate` — 6 tells (1 X-things, 5 em-dashes)
3. `hard-conversation` — 6 tells (1 X-things, 1 uncomfortable, 3 em-dashes, 1 And)
4. `ai-changing-ld` — 6 tells (1 X-things, 4 em-dashes, 1 And)
5. `why-your-proposal-died` — 5 tells (1 X-things, 1 "the real", 4 em-dashes)

## Cross-reference: Claude's confirmed verbal fingerprints (2026 external research)

Phase 1C of the audit ran fresh web searches across Pangram Labs, Bloomberry Research, Will Francis, Wikipedia "Signs of AI Writing", Frontiers in Education, and the GitHub Humanizer skill. Confirmed coverage:

| Tell | External confirmation | Present in LH corpus? |
|------|----------------------|------------------------|
| Em-dash cascade (Claude-specific) | Multiple sources | ✅ 1.9 mean, up to 5 per post |
| "It is not X. It is Y." contrastive negation | Wikipedia, Will Francis, LessWrong, Blake Stockton | ✅ 2 per corpus, plus "isn't the X. It's Y" variant in 4/16 |
| "We are not just X. We are Y." | Wikipedia "Signs of AI Writing" | ✅ Pattern present |
| Three-beat short-sentence rhythm | Pangram Labs (82% AI signature) | ✅ Moderate |
| "Here is the [thing/truth/payoff]" hedge-opener | Bloomberry, Humanizer | ✅ 1 corpus |
| Research-anecdote-sandwich predictable rhythm | GIJN | ✅ Pervasive (16/16) |
| Question-based or numbered-list endings | Multiple sources | ✅ 15/16 closes |
| "delve" / "robust" / "leverage" / "tapestry" / "comprehensive" | Pangram, Humanizer | Mostly absent (rules already filtered) |
| "In today's world/age/digital age" vague-temporal opener | Blake Stockton, AI vocab research | Not present (good baseline) |
| Tutorial-specific: numbered step bloat | Humanizer | Lower risk so far in /build/ |
| Tutorial-specific: pedagogical recap ("What we learned") | Frontiers Education | Not present (good baseline) |
| Tutorial-specific: "robust / scalable / enterprise-grade" adjective inflation | Pangram, Will Francis | Lower-frequency; preemptive ban |
| "Let's dive into" / "In this tutorial we will" tutorial signposting | Anecdotal + AI voice consensus | Not yet present in /build/; preemptive ban |

## What changed (load-bearing fixes)

Three load-bearing changes (in order of impact):

### 1. Both cloud trigger prompts rewritten

- `trig_01G4wG4UhoH1kjybdoZkuUCp` (Monday /lead/) — pushed 2026-05-04T05:43Z. Original saved at `~/.claude/plans/lh-trigger-MONDAY-original-backup-2026-05-04.md`.
- `trig_01FmF5MK27E6mCHCGVZKFbTT` (Thursday /build/) — pushed 2026-05-04T05:45Z. Original saved at `~/.claude/plans/lh-trigger-THURSDAY-original-backup-2026-05-04.md`.

Specific changes per prompt:

- Replaced fixed multi-section structural template with required ELEMENTS (loose order, flexible headers).
- Added explicit BANNED OPENERS, BANNED VOICE TICS, BANNED CADENCES, BANNED VOCABULARY sections at the top of the prompt, before structural guidance.
- Banned the section-header phrases "Hidden cause", "The symptom everyone recognizes", "A lingering thought" by name.
- Banned the formulaic action-list header "Four Things to Try" / "Three Things to Try" / "X Things You Can [verb]".
- Banned LH-specific opener patterns identified in audit: "The ones who [verb]", "Here's what I keep seeing", "Notice what".
- Banned LH-specific cadence "isn't the X. It's the Y".
- Demoted "I have a theory" and "I've been reflecting on" from opener slot (max once per quarter as opener).
- Banned tutorial signposting "Let's dive into", "In this tutorial we will", "What we learned", "Key takeaways" (Thursday only).
- Banned tutorial adjective inflation "scalable", "enterprise-grade", "production-ready" (Thursday only).
- Banned step bloat structural pattern (Thursday only).
- Added anti-self-plagiarism check on body opening (last 5 posts) AND section headers (last 5 posts) AND closing paragraph (last 5 posts).
- Replaced hardcoded leaked Telegram bot token with `$TELEGRAM_BOT_TOKEN` env var pattern; if unset, skip silently.
- Extended the executable Bash gate from 5 to 8 gates (Monday) and added a 7-gate version (Thursday). New gates: banned-phrase grep, hyphen/em-dash detection, section-header repetition vs last 5 posts, step bloat warning (build only).
- Required voice qualities reframed from "Use 'I'd argue'" (mandate) to "Direct first-person stance: state positions, don't hedge with 'I'd argue'."

### 2. Local voice files synced

- `CLAUDE.md` (lines 146–207 area) — added an "Anti-Formula Hard Bans" section after the existing Anti-AI Rules. Demoted signature-phrase openers in the Signature Phrases block.
- `~/.claude/skills/leadhuman-pipeline/SKILL.md` (Voice Rules section) — extended Anti-AI vocabulary list, added a quick-reference Anti-Formula Hard Bans section pointing to CLAUDE.md and this audit. Pre-publish executable gate extended from 6 to 8 gates with banned-phrase grep, executable em-dash detection, and section-header repetition check.

### 3. Audit + corpus rewrite (this document and Phase 4)

This audit plus the rewrites of the high-tell-density posts in Phase 4. Live-site bodies are the user-facing artifact, so they need to actually reflect the new rules.

## What stayed the same

- Pillar rotation gate (Step 0). It's working — the issue was structure, not topic selection.
- Consensus MCP for academic citation (Monday only).
- Notion Content Vault flow.
- 600–900 words /lead/, 600–800 words /build/.
- Single quotes for concepts, contractions always, no hashtags.
- No fabricated anecdotes, no hallucinated sources.
- The two model and MCP connection settings (`claude-sonnet-4-6`, Consensus + Notion).
- The cron schedules (Monday 08:03 UTC, Thursday 08:03 UTC).

## Out of scope of this audit

- Other LH content (videos, LinkedIn posts) — voice rules apply but the platform-specific drafters live elsewhere.
- The publish.py JP translation prompt — uses generic translation guidance not aligned with the new bans, but JP retranslation is handled in Phase 5 of this scrub by retranslating from the rewritten EN bodies.

## Confidence

High. Findings are quantitative, drawn from a 16-post corpus, and cross-referenced against independent third-party 2026 research on Claude fingerprints. The smoking gun (the trigger prompt mandating its own contradictions) is verbatim from the actual cloud config. The rewrites of both trigger prompts have been pushed and verified via the RemoteTrigger get response.

The only meaningful risk is that the new prompts will produce DIFFERENT output rather than BETTER output. Mitigations:

- Backups of original prompts saved (see "Load-bearing fixes" section 1).
- The first new draft fires Monday 2026-05-04 17:03 JST (today). Jay can review and revert if needed.
- The new prompts are derived from the PP scrub which Jay validated as "much better" on 2026-05-03.

---

*Audit conducted 2026-05-04 by First Councilor (Claude Opus 4.7) with parallel Explore agents. Source data: `src/content/lead/*.md`, `src/content/build/*.md`, and the two LH trigger configs retrieved via the RemoteTrigger MCP tool. Methodology mirrors the PP audit at `peak-potential-consulting/docs/ai-voice-audit-2026-05-03.md`.*
