# AI Collective — Raw — 2026-04-15

**Source:** aicollectivenewsletter@mail.beehiiv.com
**Message-ID:** 19d91abdcccc6349
**Date:** 2026-04-15

---

It's Wednesday, April 15th: This week, builders can plug AI coding agents directly into a live Shopify store, turn any Confluence page into charts or interactive apps, and deploy long-running cloud agents without building any infrastructure themselves.

TODAY'S TOP TOOLS

Shopify AI Toolkit, Your Store Controlled by Plain English

Shopify open-sourced a free plugin on April 9 that connects AI coding agents directly to your store. Point Claude Code, Cursor, or VS Code at it, and you can update products, manage inventory, run bulk SEO changes, and execute pricing rules in plain English. No dashboard login needed. It ships as an auto-updating plugin covering 16 distinct agent skills, and setup takes one or two steps.

How It Works: The toolkit builds on Shopify's Dev MCP Server and connects to Claude Code, Cursor, VS Code, Gemini CLI, and OpenAI Codex. The 16 skills cover four jobs: learning the Shopify API surface, pulling live documentation, validating code before it runs, and executing store operations through the Shopify CLI.

What You Can Do:
- Describe a product collection in plain English — the agent writes and executes the correct GraphQL API calls
- Run bulk SEO updates, discount configurations, and product image swaps without opening the admin
- Introspect the full GraphQL schema in real time before writing any code
- Validate Liquid theme and Hydrogen component code blocks before deploying

Free and MIT-licensed. One or two setup steps in Claude Code; plugin plus MCP config for Cursor and VS Code. Standard API rate limit: 1,000 cost points per minute.

Confluence Remix, Turn Any Doc Into a Visual in Seconds

Atlassian launched Remix in open beta on April 8 for Confluence Cloud users with Rovo. Highlight any section of a Confluence page — a table, a paragraph, or an entire document — and Remix generates a chart, infographic, or scorecard layered on top of it. The original content stays intact, and the visual updates automatically as the underlying page changes. Three partner agents also launched the following week, connecting Confluence pages directly into Lovable, Replit, and Gamma.

What the Partner Agents Do (three MCP-backed agents launched in open beta the week of April 13):
- Lovable: turns a product spec into a working interactive prototype
- Replit: converts a technical document into a starter app you can fork
- Gamma: transforms meeting notes into a polished presentation

Claude Managed Agents, Ship Cloud Agents Without the Infrastructure Work

Anthropic launched Claude Managed Agents in public beta on April 8. Instead of building your own agent loop, execution sandbox, and error handler from scratch, you define the task and Anthropic runs the infrastructure. The service covers sandboxed code execution, state management, context compaction, and end-to-end tracing out of the box. Early adopters include Notion, Rakuten, and Asana. It is available to all Claude API accounts today.

How It Works: You create an Agent (model, system prompt, tools), an Environment (cloud container with your packages and network rules), and a Session (the running task). Claude executes autonomously, reading files, running shell commands, browsing the web, writing and running code and streams results back via server-sent events.

Built-in Tools:
- Bash — run shell commands in the container
- File operations — read, write, edit, glob, grep
- Web search and fetch — live research and content retrieval
- MCP server connections — plug in any external tool provider

Pricing: standard Claude token rates plus $0.08 per session-hour for active runtime.

JOBS IN AI

Work at a Lab / AI Safety:
- Research Engineer / Scientist, Alignment Science — Anthropic, San Francisco, CA
- ML Engineer, Secure AI Lab — Carnegie Mellon University SEI, Pittsburgh, PA / Washington, DC
- Data Scientist, Alignment — AE Studio, Remote (USA) / Los Angeles, CA
- Insider Risk Investigator, Technical and Human Intelligence — Anthropic, San Francisco / New York / Seattle
- Standards Researcher — SaferAI, Paris / London

Work in Industry:
- ML Engineer, Physical AI — Encord, San Francisco, CA ($150K–$200K)
- Forward Deployed ML Engineer — Triomics, New York, NY ($170K–$190K)
- AI Engineering Lead — Aden, San Francisco, CA / Remote ($250K–$350K)
- Senior Software Engineer — Confido, New York, NY ($210K–$280K)
- Software Engineer, Data Platform — OneChronos, New York / Amsterdam / London / Tokyo ($115K–$200K)

Work in AI Policy / Governance:
- Policy Advisor / Senior Policy Advisor — Control AI, Washington, DC
- Senior Analyst / Counsel, AI Governance — Future of Privacy Forum, Washington, DC
- Policy Director — Institute for AI Policy and Strategy, Remote, DC / London / SF preferred
- Research Manager, AI Governance — Pivotal Research, London, UK

EVENT: MongoDB.local London: For Founders Building What's Next (Old Billingsgate, May 7)
Join AI founders at .local London to scale from prototype to production. Hear from CJ Desai, 20VC's Harry Stebbings, Sequoia, Hugging Face, and more.
