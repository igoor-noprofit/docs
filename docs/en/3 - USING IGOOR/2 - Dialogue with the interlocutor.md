## A brief history of the interlocutor in AAC software

**Traditionally, AAC software has always taken into account exclusively the user's wish to communicate**.

**The major innovation introduced by IGOOR**, made possible by generative artificial intelligence and voice recognition, consists in **transcribing the interlocutor's voice** to augment the context of the conversation and generate predictions. This **includes the interlocutor** in the dialogue process with the user, instead of always waiting for the user's communication initiative.

<div style="background:#666;color:#fff; padding: 10px"><strong>NOTE: To our knowledge, we were the first to propose this concept and to implement it</strong>, as early as our validation prototype, which we were already showing <strong>in June 2024</strong> <a style="color:#fff" target="blank" href="https://vimeo.com/969643455">in this video on Vimeo</a>.
<br><strong>If we are so proud to have done it, it is also because this idea came from Igor Novitzki, founder of our association and also affected by ALS.</strong></div>

## Voice recognition (ASR)

The default voice recognition (ASR, *Automated Speech Recognition*) is based on Groq's AI, but you can change your provider in:

*Settings > Home > Voice recognition > Configure voice recognition*

There are also several ways to trigger the transcription of the interlocutor's voice (see [[1 - Voice recognition]]).

By default, clicking on the microphone icon triggers the interlocutor's words, and

## The AI transcribes your sentence, "reasons" and generates predictions

### TRANSCRIPTION

The choice of your voice recognition model can affect the quality of the transcription. However, language models are often able to overcome transcription "hallucinations" by using the context, e.g. the ongoing conversation.

Here is an example of a sentence spoken by the interlocutor, transcribed by the AI:

![[asr_transcription.png]]

### REASONING

**The AI "reasons" before generating the answers**. This process, invisible to the user, is however important for understanding how it works, and the fact that it takes the user's preferences into consideration (in this case, food preferences):

`We need to consider Igor's preferences: prefers fish, soups, light, soft foods, dislikes heavy, likes fish, likes miso, foie gras? He likes foie de veau, foie de morue, but not heavy? He likes fish, soups, light, avoids heavy meat. He also has difficulty chewing and swallowing, prefers soft foods, fish, soups, non-spicy Asian soups. He doesn't like rice cake. So for options: fish (good), foie gras (maybe heavy and rich, but could be okay?), meat (likely heavy, not preferred), spaghettis (hard to chew, not ideal), fruits (soft, okay). So we can give positive responses for fish and maybe fruits, neutral for foie gras, negative for meat and spaghettis. Need between 3 and 6 answers total, spread across columns: left (positive), center (mitigated/alternative/ironic), right (negative). Left can have 1-2 answers, center 1-2, right 1-2. Must have at least 3 total. Provide up to 6.` `We also need to incorporate Igor's ironic style at most 1 in 6. So maybe one answer is ironic, placed maybe in center.`

**NOTE: Reasoning is not supported on all models.** Reasoning can also make the answer generation time slightly longer, but generally improves the quality of predictions.

### GENERATION AND DISPLAY OF ANSWERS

**The answers are then visually structured on three columns:**

![[../assets/flow_3_cols.png]]

**The principle is the same as for daily needs:**

- **On the left, we have "positive" answers** (in this case, the acceptance of fish or fish broth);
- **On the right, we have "negative" answers** (in this case, foods that he refuses);
- **In the center, we have two more nuanced answers**.

Several sentences can be clicked, and thus spoken through the voice synthesis, one after the other: in this specific case, the user could choose several to indicate all their preferences for the meal.

## TIPS FOR USERS

- **Clicking again on the sentence, once it has been inserted into the conversation, causes the sentence to be repeated**; useful if the other person did not hear well, or in case of a voice synthesis error.

## TIPS FOR INTERLOCUTORS

- **Use simple sentences**
- Speak with **clear enunciation**
- Provide **information that is as complete as possible, to help the AI better establish the context**
