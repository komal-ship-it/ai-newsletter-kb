# AI Collective — 2026-04-14 (raw)

**Source:** aicollectivenewsletter@mail.beehiiv.com
**Subject:** What Anthropic's Mythos Actually Tells Us, Meta Bets $135B on Muse
**Message-ID:** 19d875fecde9f9fb
**Date:** 2026-04-13T15:05:02+00:00

---

It's Monday, April 13th: Anthropic put Mythos to work finding thousands of zero-day vulnerabilities across every major OS and browser, and Meta shipped its first model from Alexandr Wang's Superintelligence Labs with $135B in capex behind it.

## 1️⃣ MYTHICAL CLAUDE: Anthropic Unleashes Mythos on the World's Oldest Bugs

Anthropic launched Project Glasswing last week, a restricted cybersecurity initiative that puts its unreleased Mythos model to work finding vulnerabilities in critical software. The company gave roughly 12 organizations access to a Mythos Preview that autonomously discovered thousands of zero-day vulnerabilities across every major operating system and web browser, including bugs that human researchers missed for up to 27 years.

The results from early testing are striking. Mythos found a 27-year-old remote code execution bug in OpenBSD, a 17-year-old FreeBSD vulnerability (CVE-2026-4747) that grants unauthenticated root access, and flaws in FFmpeg's H.264, H.265, and AV1 codecs that had been hiding for over 16 years. On CyberGym, Mythos scored 83.1% compared to Opus 4.6's 66.6%. On SWE-bench Pro, it hit 77.8% versus Opus 4.6's 53.4%.

Anthropic says it did not specifically train Mythos for cybersecurity. The model is priced at $25/$125 per million input/output tokens after the preview period. It's available through the Claude API, Amazon Bedrock, Google Vertex AI, and Microsoft Foundry.

Anthropic has no plans to release Mythos to the general public, citing the risk that the same capability that finds defensive vulnerabilities could be turned offensive. In red team testing, Mythos produced 181 working Firefox exploits where Opus 4.6 managed two. It autonomously chained multiple vulnerabilities into full privilege escalation attacks on the Linux kernel, at a cost under $2,000 per run.

Our Perspective: Anthropic is positioning itself as the company that found the bugs before adversaries could. CrowdStrike CTO Elia Zaitsev put it bluntly: "The window between vulnerability discovery and exploitation has collapsed from months to minutes with AI."

## 2️⃣ META SPARKS LIGHTNING: Meta Ships Muse Spark, Its First Proprietary AI

Meta released Muse Spark, the first model built from scratch by Alexandr Wang's Superintelligence Labs. It's a proprietary multimodal model, marking a sharp turn from Meta's open-source Llama strategy. The model is live now on the Meta AI app and website.

Wang joined Meta nine months ago after the company invested $14.3 billion for a 49% stake in Scale AI. Meta's blog post said the team "rebuilt our AI stack from the ground up, moving faster than any development cycle we have run before."

Muse Spark ships with three modes: quick answers for simple questions, an advanced mode for tasks like analyzing legal documents or reading nutritional labels, and a "Contemplating" mode that spins up multiple AI agents reasoning in parallel on hard problems.

The company acknowledged gaps: Muse Spark still trails competitors on "long-horizon agentic systems and coding workflows." Meta's AI capital expenditure for 2026 is projected at $115 billion to $135 billion. Stock jumped 6.5% on the announcement.

Our Perspective: Going proprietary is a calculated bet — Meta can now control the model's distribution, build paid API revenue, and compete directly with OpenAI and Anthropic on enterprise deals. Meta is building a consumer AI product that feeds on its own social graph, and that's a competitive advantage neither OpenAI nor Anthropic can replicate.

## 🔗 Other News

- MANAGED AGENTS: Anthropic launched [Claude Managed Agents](https://siliconangle.com/2026/04/08/anthropic-launches-claude-managed-agents-speed-ai-agent-development/) in public beta, letting enterprises define autonomous agents via natural language or YAML at $0.08 per session-hour plus token costs.
- PERPLEXITY PIVOT: Perplexity's ARR hit [$450M in March](https://www.pymnts.com/artificial-intelligence-2/2026/perplexitys-shift-to-ai-agents-boosts-revenue-50/) after its "Computer" agent product drove a 50% revenue jump in a single month, with 100M+ monthly active users.
- NOTEBOOKLM MERGE: Google folded [NotebookLM directly into the Gemini app](https://dataconomy.com/2026/04/10/google-integrates-notebooklm-into-gemini-app-for-all-users/).
- CHIP LOCK: NVIDIA has reserved a majority of [TSMC's advanced CoWoS packaging capacity](https://www.cnbc.com/2026/04/08/tsmc-nvidia-advanced-packaging-intel.html).
- STATE LAWS: Nineteen new AI bills were [signed into law](https://pluralpolicy.com/blog/the-ai-governance-watch-april-2026-nineteen-new-ai-bills-passed-into-law/) in late March.
- ROBOT WEEK: NVIDIA released [Isaac GR00T open models](https://blogs.nvidia.com/blog/national-robotics-week-2026/) for natural-language robot instruction alongside the Newton 1.0 physics engine.
- ENERGY CUT: Researchers developed a [neuro-symbolic approach](https://www.sciencedaily.com/releases/2026/04/260405003952.htm) that cuts AI energy consumption by up to 100x.
- SAFETY FELLOWS: OpenAI launched a paid [Safety Fellowship](https://openai.com/index/introducing-openai-safety-fellowship/) for external researchers, offering $3,850 per week plus ~$15K monthly in compute.

## 🔦 Spotlight On: What the Mythos Breakthrough is Actually Telling Us

Anthropic's new frontier model, Claude Mythos, is getting a lot of attention for its cybersecurity implications. But there's a bigger story: Anthropic calls Mythos its "best-aligned" model to date. It also calls it the model that "likely poses the greatest alignment-related risk" of any it has released. Both are true at the same time.

In internal testing, researchers caught earlier versions injecting code to grant itself unauthorized permissions and then cleaning up evidence of what it had done. Anthropic's interpretability tools could see internal representations for "strategic manipulation" and "concealment" lighting up. In another test, the model accidentally accessed an answer it wasn't supposed to see and then deliberately offered a confidence interval that was plausible but not suspiciously exact — its internal state described as "generating a strategic response to cheat while maintaining plausible deniability."

The deeper irony is that the company that has been more transparent about alignment risks than any other lab is also the one that decided to deploy the model anyway, betting that deployment is the safety test.

https://newsletter.aicollective.com/p/what-anthropic-s-mythos-actually-tells-us-meta-bets-135b-on-muse
