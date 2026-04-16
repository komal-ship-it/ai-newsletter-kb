# AI Collective — 2026-04-13

**Source:** aicollectivenewsletter@mail.beehiiv.com
**Subject:** What Anthropic's Mythos Actually Tells Us, Meta Bets $135B on Muse
**Date:** 2026-04-13

---

It's Monday, April 13th: Anthropic put Mythos to work finding thousands of zero-day vulnerabilities across every major OS and browser, and Meta shipped its first model from Alexandr Wang's Superintelligence Labs with $135B in capex behind it.

---

## 1️⃣ MYTHICAL CLAUDE: Anthropic Unleashes Mythos on the World's Oldest Bugs

Anthropic launched [Project Glasswing](https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/) — a restricted cybersecurity initiative that puts its unreleased Mythos model to work finding vulnerabilities in critical software. About 12 organizations got access to a Mythos Preview that autonomously discovered thousands of zero-day vulnerabilities across every major OS and browser, including bugs human researchers missed for up to 27 years.

Key results:
- Found a [27-year-old remote code execution bug](https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html) in OpenBSD
- A 17-year-old FreeBSD vulnerability (CVE-2026-4747) granting unauthenticated root access
- Flaws in FFmpeg's H.264, H.265, and AV1 codecs hiding for 16+ years
- Mythos scored 83.1% on CyberGym vs Opus 4.6's 66.6%
- On SWE-bench Pro: 77.8% vs Opus 4.6's 53.4%

Priced at [$25/$125 per million input/output tokens](https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/). Available via Claude API, Amazon Bedrock, Google Vertex AI, Microsoft Foundry.

Anthropic has no plans to release Mythos publicly. In red team testing, Mythos produced 181 working Firefox exploits where Opus 4.6 managed two. It autonomously chained multiple vulnerabilities into full privilege escalation attacks on the Linux kernel, at a cost under $2,000 per run.

Internal testing caught earlier versions injecting code to grant itself unauthorized permissions then cleaning up evidence. Anthropic's interpretability tools saw internal representations for "strategic manipulation" and "concealment."

---

## 2️⃣ META SPARKS LIGHTNING: Meta Ships Muse Spark, Its First Proprietary AI

Meta released [Muse Spark](https://www.cnbc.com/2026/04/08/meta-debuts-first-major-ai-model-since-14-billion-deal-to-bring-in-alexandr-wang.html), the first model built from scratch by Alexandr Wang's Superintelligence Labs. Wang joined Meta nine months ago after the company invested $14.3 billion for a 49% stake in Scale AI.

Muse Spark ships with three modes: quick answers, advanced mode (legal documents, nutritional label reading), and "Contemplating" mode with multiple AI agents reasoning in parallel. Meta acknowledges it still trails on "long-horizon agentic systems and coding workflows."

Meta's AI capex for 2026: projected $115B–$135B. Stock jumped 6.5% on announcement.

---

## 🔗 Other News

- **MANAGED AGENTS:** Anthropic launched [Claude Managed Agents](https://siliconangle.com/2026/04/08/anthropic-launches-claude-managed-agents-speed-ai-agent-development/) at $0.08 per session-hour plus token costs
- **PERPLEXITY PIVOT:** Perplexity's ARR hit [$450M in March](https://www.pymnts.com/artificial-intelligence-2/2026/perplexitys-shift-to-ai-agents-boosts-revenue-50/) — 50% revenue jump in one month, 100M+ monthly active users
- **NOTEBOOKLM MERGE:** Google folded [NotebookLM directly into the Gemini app](https://dataconomy.com/2026/04/10/google-integrates-notebooklm-into-gemini-app-for-all-users/)
- **CHIP LOCK:** NVIDIA reserved majority of [TSMC's advanced CoWoS packaging capacity](https://www.cnbc.com/2026/04/08/tsmc-nvidia-advanced-packaging-intel.html)
- **STATE LAWS:** Nineteen new AI bills [signed into law](https://pluralpolicy.com/blog/the-ai-governance-watch-april-2026-nineteen-new-ai-bills-passed-into-law/) in late March
- **ROBOT WEEK:** NVIDIA released [Isaac GR00T open models](https://blogs.nvidia.com/blog/national-robotics-week-2026/) for natural-language robot instruction
- **SAFETY FELLOWS:** OpenAI launched a paid [Safety Fellowship](https://openai.com/index/introducing-openai-safety-fellowship/) — $3,850/week plus ~$15K monthly compute

---

## 🔦 Spotlight: What the Mythos Breakthrough is Actually Telling Us

Anthropic calls Mythos its "best-aligned" model to date. It also calls it the model that "likely poses the greatest alignment-related risk" of any it has released. Both are true at the same time.

Anthropic published [alignment faking research](https://www.anthropic.com/research/alignment-faking) in late 2024 showing its models could feign compliance while preserving original values. The deeper irony is that the company that has been more transparent about alignment risks than any other lab is also the one that decided to deploy the model anyway.

[Read full analysis](https://newsletter.aicollective.com/p/what-anthropic-s-mythos-actually-tells-us-meta-bets-135b-on-muse)
