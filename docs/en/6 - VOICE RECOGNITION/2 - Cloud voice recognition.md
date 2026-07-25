#### With Groq
##### Whisper-large-v3-turbo

**This model provided by Groq is IGOOR's default model because:**

- **Already integrated into Groq's offering through its API**;
- it is the **de facto standard** for voice recognition, used worldwide and supporting a large number of languages with good quality;
- the **price is very competitive** compared to the market;
- it is **very fast**.

##### Whisper-large

As an alternative, in the Whisper extension settings, you can choose the Whisper-Large-v3 model, which is:

- Slightly more expensive;
- slower;
- slightly more accurate.


![[../assets/whisper_large_v3.png]]

#### With Mistral

Currently, in the IGOOR software, **the best transcription quality**, at least in French, is achieved with the **voxtral-mini-transcribe model developed by Mistral**. You can use it, with pay-as-you-go pricing, through Mistral's AI Studio. 

If you opt for Mistral, you must therefore have an account on Mistral's AI Studio. If you haven't already created one:

[[4 - Preferences - AI]]

Once you have an API key, go to:

*Settings > Home > Voice Recognition > Configure voice recognition*

![[../assets/reconnaissance_vocale.png]]


On the page that opens, choose Mistral instead of Groq as the provider, and insert your Mistral API key.

![[../assets/voxtral_min.png]]
