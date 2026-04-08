# Superhuman Code — Raw — 2026-04-07

**Message ID:** 19d631c1d5670323
**From:** thecode@mail.joinsuperhuman.ai
**Subject:** 🎙️ Microsoft drops three new AI models
**Date:** 2026-04-06T14:04:39Z

---

Welcome back. Microsoft is officially stepping out of OpenAI's shadow. They just dropped a new family of specialized AI models, and the early benchmarks are already beating some familiar names.

Also: 15 things that crash vibe-coded apps in production, ship iOS apps without Xcode, and what's behind OpenAI's IPO tension.

Today's Insights:
- Powerful new updates and hacks for devs
- Tech's fastest-growing role has a trust problem
- How to turn Figma designs into code with Codex
- Trending social posts, top repos, and more

---

TODAY IN PROGRAMMING

Microsoft drops three new AI models for speech, voice, and images: The software giant just dropped its new MAI model family on Microsoft Foundry. MAI-Transcribe-1 is already topping speech-to-text benchmarks in 25 languages, beating out OpenAI's Whisper and Google's Gemini with speeds 2.5x faster than Azure's current batch transcription. There's also MAI-Voice-1, which can clone a custom voice from just seconds of audio, and MAI-Image-2, which is now a top-three contender on Arena AI while generating images twice as fast.

Anthropic cuts third-party tool support from Claude plans: The AI lab just cut third-party tool support from its subscription plans, citing high demand that their current pricing couldn't handle. While tools like OpenClaw are out, you can still connect via discounted usage bundles or an API key, and existing subscribers are getting a one-time credit to cover the transition. OpenAI capitalized on the move immediately, pointing out that ChatGPT Plus still works seamlessly with OpenClaw, OpenCode, and Cline, while also promoting their open-source Codex App Server for custom builds.

Karpathy turns LLMs into personal knowledge engines: The OpenAI co-founder just pitched a new way to share projects: skip the code and share the concept, then let an AI agent build it for you. His first example uses LLMs to generate interconnected Markdown knowledge bases that are stored locally and viewable in tools like Obsidian. You own the data, the format is universal, and you can plug in any AI provider. Builders like Farza Majeed are already jumping on board, creating personal wikis from thousands of diary entries.

---

INSIGHT

Tech's fastest-growing role has a trust problem

AI just minted a new job title. The forward-deployed engineer (FDE) barely existed outside Palantir until last year. Now, postings for the role have spiked 10x, with companies like Salesforce building out entire teams. FDEs embed with customers to make AI work in production, proving enterprise AI needs far more human hand-holding than expected.

But engineers aren't biting. The Wall Street Journal reports only 10% interest from talent, as many see it as a high-stress, low-prestige consulting gig. One dev even quit after four weeks, citing zero coding and too much client management.

The title often overpromises. While FDEs at OpenAI or Ramp build core products, most other roles are just sales support. Engineers usually spot this gap during the interview or shortly after starting.

Ultimately, AI still needs a human touch. Bridging the gap between a demo and production in messy enterprise environments requires writing code for legacy systems. Until these roles offer real engineering substance, the talent gap will only widen.

---

IN THE KNOW: What's trending on socials and headlines

- Auto Apply: This project scans career pages, rewrites your CV, and fills applications automatically. One dev used it to land a job after 700+ submissions (1.8M views).
- Vibe Check: Most vibe-coded apps crash in production. This thread covers the 15 most common failure points and how to fix them.
- Supply Chain Attack: After attackers slipped a trojan into Axios npm's most popular HTTP client, the maintainer posted how it was compromised (1.5M views).
- Second Brain: Karpathy shared the 7-step setup he uses to build a personal knowledge base with just folders, text files, and a schema (1M views).
- Ship Without Xcode: This Codex workflow lets you build and ship iOS apps entirely from the command line. One dev did it in under 7 minutes.
- Free Stanford Lecture: Stanford just dropped the full first lecture of its new AI systems course (CS153).
- IPO Tension: OpenAI's CFO has privately raised concerns about Altman's aggressive spending and his push to IPO this year.

---

AI CODING HACK: How to turn Figma designs into code with Codex

Every frontend engineer knows the drill. A designer hands you a Figma file, and you spend the next few hours manually translating spacing, tokens, and layout into components. Codex can now do that translation for you using its Figma and Playwright skills.

Copy a link to the exact Figma frame you want built, then paste this prompt into Codex:

"Implement this Figma design in the current project using the Figma skill.
Requirements:
- Start with get_design_context for the exact node or frame.
- Run get_screenshot for the exact variant before you start coding.
- Reuse the existing design system components and tokens.
- Make the page responsive on desktop and mobile.
Validation:
- Use Playwright to check that the UI matches the reference and iterate until it does."

Codex pulls design context from Figma's MCP server and generates code that matches your repo's patterns. It then uses Playwright to test the result in a live browser, iterating automatically until the UI perfectly matches the original design.

---

TOP & TRENDING RESOURCES

Top Tutorial: How to use spec-driven development with AI agents — You'll learn how to write clear specs, set strict constraints, and break down complex features into manageable tasks.

Top Repo: Agent Skills (by Google Cloud AI's Director) — A repo focused on production-grade skills for AI coding agents, providing packaged workflows and quality gates.

Trending Paper: AI Agent Traps (by Google) — As AI agents browse the web, they're running into "AI Agent Traps", hidden malicious content built to trick or exploit them. Researchers mapped out six different types of these attacks.
