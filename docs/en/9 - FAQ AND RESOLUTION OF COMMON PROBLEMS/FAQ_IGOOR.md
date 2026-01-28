# FAQ IGOOR – Frequently asked questions

## General
**Q: What is IGOOR?**
A: IGOOR is an open-source conversational application, controllable by voice or eye-tracking, designed for people with impaired communication (e.g., ALS).

**Q: Is IGOOR free?**
A: Yes. The software is free and open-source. Some features (TTS, voice cloning, AI) use third-party services that may be paid; IGOOR is not affiliated with any of them.

**Q: Where are my memories stored?**
A: All memories (short-term, long-term, extracted) are stored locally on your computer. They are sent to AI providers only when a prediction requires them.

**Q: Where is my cloned voice stored?**
A: Audio samples are sent to cloud services (Speechify, Elevenlabs...) to create the clone. The API key for your account is stored locally so IGOOR can use it.

## Installation
**Q: How to install IGOOR?**
A: 1. Download the file `IGOOR-Setup.exe` (see *2 - Download IGOOR.md*).
2. Run it and accept the installation from an unknown source.
3. Follow the screens: license → destination → installation.
4. Once installed, launch IGOOR from the start menu.

**Q: What hardware is required?**
A: Windows 10/11, PC or tablet. No GPU is required; AI features use Groq, a cloud-based AI provider.

**Q: Does the installation fail with ffmpeg or Edge?**
A: Check that `ffmpeg` and the Edge browser are already installed (images `ffmpeg_already_installed.png`, `edge_already_installed.png`). Otherwise, download them and relaunch the installer.

## Minimal setup
**Q: What are the setup steps?**
A: See *1 - Minimal setup.md*:
- Set the memory storage directory.
- Enter the Groq API key (see `groq_account_login.png`).
- Choose the TTS engine (see *1 - Choose your TTS voice synthesis system.md*).

## Text-to-speech (TTS)
**Q: Which TTS synthesizers are compatible?**
A: IGOOR supports:
- **Microsoft Speech API** (Windows).
- **Elevenlabs** (cloud).
- **Speechify** (cloud).
Choose the system in *1 - Choose your TTS voice synthesis system.md*.

**Q: How to change voice or language?**
A: In Settings → TTS, select the engine and then the voice/language listed.

## Eye-tracking / TD Control
**Q: How to use IGOOR with TD Control (eye-tracking)?**
A: Follow the guide *1 - TD Control and eye-tracking.md*:
1. Install the TD Control software.
2. Enable "click-by-dwell".
3. Map the "activate voice recognition" button to the desired eye gesture.
4. Restart IGOOR.

## External buttons & voice recognition
**Q: Can I trigger voice recognition with an external button?**
A: Yes. Plug in a compatible button (USB, Bluetooth) and configure it in *2 - External button for voice recognition.md*.

## Memory
**Q: What is the difference between short-term and long-term memory?**
A: - **Short-term**: recent conversations, kept for two weeks.
- **Long-term**: persistent information (e.g., preferences, medical history) stored permanently.
See *1 - Types of memory.md* for details.

**Q: How to automatically extract information from my documents?**
A: Use the "Memory extracted from your documents" tool (*2 - Memory extracted from your documents.md*): select the folder, run the analysis, then import the summaries into long-term memory.

## AI & Groq
**Q: How to configure the Groq API key?**
A: 1. Create a Groq account.
2. Copy the key (`groq_key.png`).
3. Open IGOOR → Preferences → AI → paste the key (`copy_api_key.png`/`paste_api_key.png`).

## Quick buttons
**Q: What are "quick buttons"?**
A: Configurable shortcuts (e.g., "Call the physiotherapist", "Ask for the weather"). See *5 - Quick buttons.md* to create or modify actions.

## Auto-fill
**Q: How to enable auto-fill?**
A: In *4 - Auto-fill.md*, enable the "Auto-fill" feature which fills text fields from long-term memory.

## Common issues
**Q: Voice recognition no longer responds?**
A: - Check the external button (cable, battery).
- Make sure the microphone works (Windows sound panel).
- Restart IGOOR.

**Q: TTS doesn't speak?**
A: - Confirm the selected TTS engine.
- Test system sound.

**Q: The app crashes on startup?**
A: - Check that `ffmpeg` is installed (`ffmpeg_already_installed.png`).

---
*This FAQ will be enriched as user feedback comes in.*