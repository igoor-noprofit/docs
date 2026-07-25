### From IGOOR v1 onwards:

- Simply select the **Sherpa-ONNX (local)** model as the provider.
- Select the large size (recommended for quality) or the small size (only if transcription is too slow)

When you save the settings, if it's the first time you use the local model, IGOOR will download the model to your computer. This may take a few minutes. You don't need to restart.

--- 
### For versions prior to v1:

Go to:

*Settings > Extensions > ASR*

- disable the ASR JAVASCRIPT module
- enable the VOSK module
- save the global settings

Restart IGOOR.

Vosk voice recognition requires an amount of RAM that reaches 3GB for the large model. You can change the model size in the Vosk plugin settings if your RAM is not sufficient.

**IMPORTANT: the VOSK extension has been replaced by the Sherpa-ONNX model in version 1, and it will no longer be supported.**
