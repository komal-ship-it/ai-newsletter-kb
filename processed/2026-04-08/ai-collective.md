# AI Collective — 2026-04-08

**Source:** aicollectivenewsletter@mail.beehiiv.com
**Date:** 2026-04-08
**Original items:** 7

## Key Announcements
- **ElevenMusic launched April 1** — Free iOS app from ElevenLabs that generates full songs from text prompts. 7 songs/day free; $9.99/month Pro. ElevenLabs raised $500M Series C at $11B valuation in February 2026. Competes with Suno and Udio.
- **Google AI Edge Eloquent launched April 6** — iOS app with fully on-device speech-to-text (no cloud upload). Powered by Gemma ASR model. Free, no usage caps. Auto-removes filler words. Works offline after initial model download.
- **Vox (Noah Labs) receives FDA Breakthrough Device designation** — 5-second daily voice recording detects heart failure 21 days before hospitalization. Trained on 3M+ voice samples. Validated at Mayo Clinic, UCSF, and 3 other sites. EU MDR approval targeted mid-2026.
- **LiteRT-LM released** — Google's on-device model runtime supporting Gemma model family on Android, iOS, desktop, and Raspberry Pi. Same stack as Eloquent, now open for builders.

## Tools & Products
- **ElevenMusic** — iOS app: text prompt → full song in seconds. Genre, mood, lyrics control. 7 songs/day free. Remixes from public tracks supported. Live stations by mood (Focus, Energy, Relax, Late Night, Cosmic, Chill). | https://apps.apple.com/us/app/elevenmusic-by-elevenlabs/id6755965224 | https://elevenlabs.io/music | Effort: quick-win
- **Google AI Edge Eloquent** — On-device iOS transcription. Fully offline after one-time Gemma model download. No account, no cloud, no usage cap. Auto-strips filler words, copies clean text to clipboard. | https://apps.apple.com/us/app/google-ai-edge-eloquent/id6756505519 | Effort: quick-win
- **Vox (Noah Labs)** — 5-second daily voice recording for cardiac congestion early detection. Currently in clinical validation — not yet consumer-available. For health systems and clinical research partners. | https://www.noah-labs.com/nl-vox | Effort: major (enterprise/clinical)
- **LiteRT-LM** — Open SDK for on-device Gemma ASR on Android, iOS, desktop, Raspberry Pi. For builders in healthcare, legal, enterprise where audio privacy matters. | https://ai.google.dev/edge/litert-lm | Effort: weekend

## Techniques & Methods
- **On-device ASR integration pattern** — For privacy-sensitive use cases: use LiteRT-LM + Gemma ASR model family. One-time model download, all inference local, no audio leaves the device. Applicable to healthcare, legal, enterprise transcription products.
- **Mobile music generation API strategy** — ElevenLabs' ElevenMusic positions the company's music generation capability for API access. Pattern: launch consumer app first to validate UX, then expose API for B2B builders. Watch for ElevenLabs music API release.

## Research Papers
- None today.

## Industry Trends
- **On-device AI vs. cloud AI** — Eloquent is Google's consumer proof-of-concept that privacy-first on-device transcription can match cloud quality. Positions against Wispr Flow (cloud-dependent). LiteRT-LM makes this accessible to builders.
- **Voice as a medical diagnostic modality** — Vox demonstrates vocal fold acoustics as a measurable biomarker for cardiac congestion, detectable 21 days before clinical presentation. FDA Breakthrough designation fast-tracks the regulatory timeline.
- **ElevenLabs full audio platform strategy** — $500M raise + $11B valuation supports a platform play: voice cloning + narration + music in one product. Music API for builders is a logical next step.

## Actionable Items
- [ ] Download and test Google AI Edge Eloquent for offline transcription — evaluate for any privacy-sensitive use case — *quick-win* — https://apps.apple.com/us/app/google-ai-edge-eloquent/id6756505519 | action-2026-04-08-006
- [ ] Try ElevenMusic free tier (7 songs/day) — assess for audio-first or creator-facing product integrations — *quick-win* — https://elevenlabs.io/music | action-2026-04-08-007
- [ ] Review LiteRT-LM for on-device Gemma ASR in any current or planned healthcare/legal/enterprise project — *weekend* — https://ai.google.dev/edge/litert-lm | action-2026-04-08-008
- [ ] Track Noah Labs Vox for clinical partnership opportunities — EU MDR approval targeted mid-2026; US trial starting soon — *quick-win* (monitor) | action-2026-04-08-009

## Notable Links
- https://newsletter.aicollective.com/p/elevenmusic-google-eloquent-and-heart-failure-detection-by-voice — Full issue
- https://ai.google.dev/edge/litert-lm — LiteRT-LM (on-device Gemma ASR SDK)
- https://www.noah-labs.com/nl-vox — Vox by Noah Labs
- https://elevenlabs.io/music — ElevenMusic product page
- https://luma.com/ip1wjj8i — ThinkingAI x MiniMax event RSVP (April 16, Computer History Museum)
