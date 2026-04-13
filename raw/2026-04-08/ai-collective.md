# AI Collective — Raw — 2026-04-08

**Message ID:** 19d6d9f4310a4674
**From:** aicollectivenewsletter@mail.beehiiv.com
**Subject:** ElevenMusic, Google Eloquent, and Heart Failure Detection by Voice

It's Wednesday, April 8th: This week, builders can generate full songs on their phone with ElevenMusic, capture speech with on-device AI using Google Eloquent, and study how Vox earned FDA Breakthrough status by detecting heart failure 21 days before hospitalization.

---

## ElevenMusic: Turn a Text Prompt into a Full Song, Right on Your Phone

ElevenLabs, the company behind some of the most widely used AI voice technology, launched ElevenMusic on April 1, a free iOS app that generates songs from natural language prompts. Describe a genre, set a mood, choose whether you want lyrics, and the app builds a full track in seconds. With a free tier covering seven songs a day and a $9.99/month Pro option, ElevenLabs is taking its first shot at mobile music generation, a space currently led by Suno and Udio.

ElevenMusic runs on a single prompt input: describe genre, writing style, and mood, and the app handles the rest. The free tier allows seven songs per day. Songs can be remixed from other users' public tracks (remixes count toward the daily limit), and the app includes curated live stations and daily mixes organized by mood: Focus, Energy, Relax, Late Night, Cosmic, and Chill.

ElevenLabs raised a $500M Series C at an $11B valuation in February 2026. ElevenMusic is a clear move toward building a full audio platform, with voice cloning, narration, and music creation all in one product. For builders shipping audio-first or creator-facing apps, API access for music generation is a logical next step from ElevenLabs, and worth tracking.

iOS App: https://apps.apple.com/us/app/elevenmusic-by-elevenlabs/id6755965224
Product page: https://elevenlabs.io/music

---

## Google AI Edge Eloquent: Dictation That Runs Entirely on Your Phone

Google quietly pushed an iOS app called AI Edge Eloquent to the App Store on April 6, and its defining feature is what it doesn't do. It doesn't send your audio to the cloud. The app downloads Google's Gemma speech recognition model directly to your phone, transcribes everything locally, and requires no internet connection after the initial setup. It's free, with no usage caps, and goes directly at tools like Wispr Flow that depend on cloud uploads for every recording.

After a one-time download of the on-device Gemma ASR model, all transcription runs locally. No audio reaches Google's servers, no account is required, and it works fully offline. When you pause recording, the app automatically removes filler words ("um," "uh," mid-sentence corrections) and copies clean prose to your clipboard.

Eloquent is Google AI Edge's consumer proof-of-concept for on-device ASR, but the underlying stack is open. LiteRT-LM (https://ai.google.dev/edge/litert-lm), released this week, supports the same Gemma model family on Android, iOS, desktop, and Raspberry Pi. If you're building for healthcare, legal, or enterprise use cases where audio privacy matters, this is the model family worth integrating.

iOS App: https://apps.apple.com/us/app/google-ai-edge-eloquent/id6756505519
Gemma ASR: https://ai.google.dev/gemma
Google AI Edge: https://ai.google.dev/edge

---

## Vox: A Daily 5-Second Voice Recording That Screens for Heart Failure

Heart failure causes over a million US hospitalizations each year, and the clinical problem is usually the same: patients deteriorate at home for days or weeks before anyone notices. Noah Labs built Vox to change that detection window. The system analyzes a 5-second daily voice recording to identify acoustic changes linked to cardiac congestion, sometimes 21 days before hospitalization becomes necessary. In April, the FDA granted Vox Breakthrough Device designation, fast-tracking US regulatory review.

Vox detects changes in vocal fold acoustics linked to pulmonary congestion and fluid overload — physiological shifts that appear in the voice before they become clinically obvious. The model was trained on more than 3 million voice samples and validated across five sites including the Mayo Clinic and UCSF. Patients record a 5-second clip daily through a phone; clinicians receive early-warning alerts when the model detects concerning patterns.

FDA Breakthrough Device designation means the FDA has prioritized the review timeline, not that approval is granted. Noah Labs expects to start its US clinical trial shortly. EU MDR approval is targeted for mid-2026. The product is currently in clinical validation, available to health systems and clinical research partners.

Product page: https://www.noah-labs.com/nl-vox

---

## Jobs in AI

### Lab / AI Safety Roles

- RESEARCH SCIENTIST — Center for AI Safety | San Francisco, CA (Competitive Salary) | https://jobs.lever.co/aisafety/0e911ab2-89e0-4936-83e6-034f7e2f8977
- SENIOR RESEARCH ENGINEER — Center for AI Safety | San Francisco, CA (Competitive Salary) | https://jobs.lever.co/aisafety/e8167e84-8669-4644-961c-e5fd5b5f4318
- FULL STACK CLOUD ENGINEER, AI SECURITY PLATFORM — HiddenLayer | Remote, USA | https://job-boards.greenhouse.io/hiddenlayer/jobs/5100067007
- RESEARCH SCHOLAR — Institute for Law and AI | Remote/Global ($100,000–$175,000 · closes Apr 17) | https://law-ai.org/career/research-scholar-2026/
- CHIEF OF STAFF — Institute for Law and AI | Remote/Global ($130,000–$250,000 · closes Apr 24) | https://law-ai.org/career/cos/

### Industry Roles

- FOUNDING ENGINEER — AgentMail | San Francisco, CA ($150,000–$250,000 + 0.5–2% equity) | https://www.ycombinator.com/companies/agentmail/jobs/x66bmSk-founding-engineer
- FOUNDING ENGINEER, AI/ML — Pax Historia | San Francisco, CA ($150,000–$240,000 + 0.25–1% equity) | https://www.ycombinator.com/companies/pax-historia/jobs/qK7Wj6I-founding-engineer-ai-ml
- STAFF AI SYSTEMS ENGINEER — Flock Safety | Remote, USA ($200,000–$240,000) | https://www.ycombinator.com/companies/flock-safety/jobs/rd2Qy51-staff-ai-systems-engineer
- STAFF AI ENGINEER — Podium | Lehi, UT / Remote ($190,000–$215,000) | https://www.ycombinator.com/companies/podium/jobs/qgKxAEM-staff-ai-engineer-usa
- FOUNDING AI ENGINEER — Weave | San Francisco, CA ($150,000–$200,000 + Equity) | https://www.ycombinator.com/companies/weave-3/jobs/SqFnIFE-founding-ai-engineer

### AI Policy / Governance Roles

- POLICY DIRECTOR — Institute for AI Policy and Strategy | Washington, DC / Remote ($141,000–$180,000) | https://www.iaps.ai/policy-director
- SPECIAL PROJECTS ASSOCIATE — Epoch AI | Remote, Global ($75,000–$100,000) | https://jobs.lever.co/epoch-ai/99d526d1-6b60-4e93-bb31-91000d7ef732
- DIRECTOR OF POLICY — CivAI | Remote, Global ($130,000–$200,000) | https://civai.org/jobs/director-of-policy
- DIRECTOR OF PROGRAMS — Institute for Law and AI | Remote/Global ($130,000–$240,000 · closes Apr 24) | https://law-ai.org/career/director-of-programs-2026/
- DIRECTOR OF OPERATIONS / COO — Institute for Law and AI | Remote/Global ($150,000–$280,000 · closes Apr 24) | https://law-ai.org/career/director-of-operations-coo/

---

## Community Notes

### SF Launch: ThinkingAI x MiniMax @ the Computer History Museum (April 16)

On April 16, ThinkingAI is launching at the Computer History Museum in Silicon Valley. The event brings together leaders from Google DeepMind, MiniMax, and leading AI startups and investors to discuss the future of agentic enterprise systems. Hosted by Brandon Nader (VP, Marketing, ThinkingAI), with panels led by Dasha Shunina (Forbes Contributor).

RSVP: https://luma.com/ip1wjj8i

---

About the Authors:

Noah Frank — researcher, innovation strategist, and ex-founder thinking and writing about the future of AI. His work explores the economics of emerging technology and organizational strategy. https://noahsfrank.com/impact

Joy Dong — news editor, writer, and entrepreneur at the forefront of the emerging tech landscape. Former educator turned media strategist; writes TEA (https://tea2025.substack.com/).

Source URL: https://newsletter.aicollective.com/p/elevenmusic-google-eloquent-and-heart-failure-detection-by-voice
# AI Collective — The Byte — 2026-04-07

**Source:** aicollectivenewsletter@mail.beehiiv.com
**Subject:** The Byte: AI Is the Next Printing Press
**Author:** Sophie Levy (Founder & CEO, The Magnet Collective)
**Date:** 2026-04-07

## Raw Body

Essay: "Human Intelligence Will Decide If AI Helps or Hurts Workplaces & Community"

Main thesis: AI's most consequential effects will be governed not by technical capability alone, but by the human capacities surrounding its adoption. Like the printing press, AI becomes corrosive when used to evade interpersonal difficulty, and constructive when it extends and reinforces capacities developed in person.

Key arguments:
1. Humans must be taught human skills locally, relationally, and in person.
2. Those skills should then be reinforced and scaled through AI tools.

The printing press parallel:
- Scribes chased printing presses out of town fearing job loss
- Knowledge became accessible to masses, destabilizing institutional power
- By mid-18th century, became one of history's greatest equalizers
- Today: AI adoption is happening on organizational timescales — can't wait centuries to adapt

Key quote: "When AI becomes a substitute for discomfort, it weakens social trust and productivity. When it becomes a rehearsal for it, it strengthens workforce performance."

Example model:
- The Magnet Collective (themagnetcollective.net) — early-career professionals build communication, collaboration, and decision-making skills by leading real capstone projects
- Tuffy (tough.day) — AI tool that reinforces reflective practice, expands access, allows skill development at scale

WEF 2025 white paper: employers prioritize analytical thinking, creativity, resilience, and leadership; uncertainty about which genAI will meaningfully improve.
Link: https://reports.weforum.org/docs/WEF_New_Economy_Skills_Unlocking_the_Human_Advantage_2025.pdf

Reference: Yudkowsky & Soares "If Anyone Builds It, Everyone Dies" — "Intelligence is about two fundamental types of work: the work of predicting the world, and the work of steering it."

Conclusion: The future of workplaces won't be decided by what AI can do, but by what we demand humans do first.

---

Premier Partner: Roam (ro.am) — virtual workspace with shared spaces, private rooms, built-in AI tools

Newsletter URL: https://newsletter.aicollective.com/p/the-byte-ai-is-the-next-printing-press
