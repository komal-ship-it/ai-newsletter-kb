# AI Collective Newsletter — Raw — 2026-04-08

**Message ID:** 19d6d9f4310a4674
**Subject:** ElevenMusic, Google Eloquent, and Heart Failure Detection by Voice
**From:** aicollectivenewsletter@mail.beehiiv.com
**Date:** 2026-04-08T15:04:05+00:00

---

It's Wednesday, April 8th: This week, builders can generate full songs on their phone with ElevenMusic, capture speech with on-device AI using Google Eloquent, and study how Vox earned FDA Breakthrough status by detecting heart failure 21 days before hospitalization.

---

TODAY'S TOP TOOLS

### ElevenMusic: Turn a Text Prompt into a Full Song, Right on Your Phone

ElevenLabs, the company behind some of the most widely used AI voice technology, launched ElevenMusic on April 1, a free iOS app that generates songs from natural language prompts. Describe a genre, set a mood, choose whether you want lyrics, and the app builds a full track in seconds. With a free tier covering seven songs a day and a $9.99/month Pro option, ElevenLabs is taking its first shot at mobile music generation, a space currently led by Suno and Udio.

ElevenMusic runs on a single prompt input: describe genre, writing style, and mood, and the app handles the rest. The free tier allows seven songs per day. Songs can be remixed from other users' public tracks, and the app includes curated live stations and daily mixes organized by mood: Focus, Energy, Relax, Late Night, Cosmic, and Chill.

ElevenLabs raised a $500M Series C at an $11B valuation in February 2026. ElevenMusic is a clear move toward building a full audio platform, with voice cloning, narration, and music creation all in one product.

---

### Google AI Edge Eloquent: Dictation That Runs Entirely on Your Phone

Google quietly pushed an iOS app called AI Edge Eloquent to the App Store on April 6, and its defining feature is what it doesn't do. It doesn't send your audio to the cloud. The app downloads Google's Gemma speech recognition model directly to your phone, transcribes everything locally, and requires no internet connection after the initial setup. It's free, with no usage caps, and goes directly at tools like Wispr Flow that depend on cloud uploads for every recording.

After a one-time download of the on-device Gemma ASR model, all transcription runs locally. No audio reaches Google's servers, no account is required, and it works fully offline. When you pause recording, the app automatically removes filler words and copies clean prose to your clipboard.

Eloquent is Google AI Edge's consumer proof-of-concept for on-device ASR. LiteRT-LM, released this week, supports the same Gemma model family on Android, iOS, desktop, and Raspberry Pi. If you're building for healthcare, legal, or enterprise use cases where audio privacy matters, this is the model family worth integrating.

---

### Vox: A Daily 5-Second Voice Recording That Screens for Heart Failure

Heart failure causes over a million US hospitalizations each year, and the clinical problem is usually the same: patients deteriorate at home for days or weeks before anyone notices. Noah Labs built Vox to change that detection window. The system analyzes a 5-second daily voice recording to identify acoustic changes linked to cardiac congestion, sometimes 21 days before hospitalization becomes necessary. In April, the FDA granted Vox Breakthrough Device designation, fast-tracking US regulatory review.

Vox detects changes in vocal fold acoustics linked to pulmonary congestion and fluid overload, physiological shifts that appear in the voice before they become clinically obvious. The model was trained on more than 3 million voice samples and validated across five sites including the Mayo Clinic and UCSF. Patients record a 5-second clip daily through a phone; clinicians receive early-warning alerts when the model detects concerning patterns.

FDA Breakthrough Device designation means the FDA has prioritized the review timeline, not that approval is granted. Noah Labs expects to start its US clinical trial shortly. EU MDR approval is targeted for mid-2026.

---

JOBS IN AI

Work at a Lab / AI Safety:
- Research Scientist — Center for AI Safety | San Francisco, CA
- Senior Research Engineer — Center for AI Safety | San Francisco, CA
- Full Stack Cloud Engineer, AI Security Platform — HiddenLayer | Remote, USA
- Research Scholar — Institute for Law and AI | Remote/Global ($100,000–$175,000, closes Apr 17)
- Chief of Staff — Institute for Law and AI | Remote/Global ($130,000–$250,000, closes Apr 24)

Work in Industry:
- Founding Engineer — AgentMail | San Francisco, CA ($150,000–$250,000 + 0.5–2% equity)
- Founding Engineer, AI/ML — Pax Historia | San Francisco, CA ($150,000–$240,000 + equity)
- Staff AI Systems Engineer — Flock Safety | Remote, USA ($200,000–$240,000)
- Staff AI Engineer — Podium | Lehi, UT / Remote ($190,000–$215,000)
- Founding AI Engineer — Weave | San Francisco, CA ($150,000–$200,000 + Equity)

Work in AI Policy / Governance:
- Policy Director — Institute for AI Policy and Strategy | Washington, DC / Remote ($141,000–$180,000)
- Special Projects Associate — Epoch AI | Remote, Global ($75,000–$100,000)
- Director of Policy — CivAI | Remote, Global ($130,000–$200,000)
- Director of Programs — Institute for Law and AI | Remote/Global ($130,000–$240,000, closes Apr 24)
- Director of Operations / COO — Institute for Law and AI | Remote/Global ($150,000–$280,000, closes Apr 24)

---

COMMUNITY NOTES

SF Launch | ThinkingAI x MiniMax @ the Computer History Museum (April 16)
On April 16, ThinkingAI is launching at the Computer History Museum in Silicon Valley. The event brings together leaders from Google DeepMind, MiniMax, and leading AI startups and investors to discuss the future of agentic enterprise systems.
