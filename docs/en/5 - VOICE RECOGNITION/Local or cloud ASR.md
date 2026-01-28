Depending on your device's technical capabilities, the performance you want to achieve, and the budget you want to spend, you can choose between on-device speech recognition (ASR, *Automated Speech Recognition*) using the Vosk model or cloud-based recognition.

## Cloud-based ASR

### Mistral

Currently, on the IGOOR software, **the best transcription quality**, especially in French, is achieved using the **voxtral-mini-transcribe model developed by Mistral**. You can use it on a pay-per-use basis through Mistral's AI Studio.

If you choose Mistral, you must create an account on Mistral's AI Studio:

![[../assets/Pasted image 20251211105340.png]]

[Subscribe to Mistral and create an API key](https://docs.mistral.ai/getting-started/quickstart)

Once you obtain an API key, go to:

Settings > Extensions > ASR JAVASCRIPT

And click on the settings icon for the Whisper extension.

Choose Mistral instead of Groq as the provider, and insert your API key.

### Whisper

**The second best option supported by IGOOR is Whisper-large-v3, provided by Groq.** This is the default option because:

- It is already integrated into Groq's offering through its API;
- this model is the de facto standard for speech recognition, widely used around the world and supports a large number of languages with sufficient quality;
- the price is very competitive compared to the market.

As an alternative, in the settings of the Whisper extension, you can choose the Whisper Large v3 Turbo model, which is:

- cheaper
- faster
- less accurate.

![[../assets/Pasted image 20251211105416.png]]

## On-device ASR

Go to:

Settings > Extensions > ASR

- disable the ASR JAVASCRIPT module
- enable the VOSK module

Restart IGOOR.

VOSK is intended for on-device use, for those who do not want to pay for a speech recognition service or for privacy reasons.

**On-device speech recognition requires a significant amount of RAM, up to 3GB for the large model. You can change the model size in the Vosk plugin settings if your RAM is insufficient.**