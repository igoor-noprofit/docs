## Hardware requirements

- A PC or tablet running **Windows 10/11**
- **Minimum resolution: 1280x960**
- Recommended resolution: 1920x1080 (Full HD) or higher
- **Recommended RAM: 16 GB or more**

## Quick setup: running in the cloud

The simplest and fastest way to use IGOOR is to rely on Groq's free services — Groq is a cloud provider of AI and speech recognition. 
You will only need:

- **An internet connection** (fiber optic or ADSL preferred)
- **A Groq API key (free or paid)**

NOTE: From version 1 onward, IGOOR also supports other providers, such as the French provider Mistral (for AI / speech recognition) and Cerebras (AI only). See [[4 - Preferences - AI]]

### How to get a free Groq API key

You can request a developer key from Groq, a cloud provider of AI inference.

[Get a Groq :key:](https://console.groq.com/keys){ .md-button target=_blank}

**IMPORTANT: We are neither partners with nor affiliated to Groq.**

### Requirements for 100% local operation

**NOTE: From IGOOR version 1 onward, you no longer need an internet connection if you use the local options for all the services.** The internet connection will however still be required when activating the various options.

Running 100% locally requires:

1) Installing on your PC a large language model (LLM) that exposes an OpenAI-compatible endpoint. **Today, this requires an extremely powerful PC to achieve prediction quality and speed comparable to cloud solutions.**
2) Using the Sherpa-ONNX model for local speech recognition (see [[2 - Cloud voice recognition]])
3) Keeping the Windows synthesis voice (see [[1 - Choosing your TTS voice synthesis system]])

