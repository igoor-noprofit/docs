#### Con Groq
##### Whisper-large-v3-turbo

**Questo modello fornito da Groq è il modello predefinito di IGOOR perché :**

- **Già integrato nell'offerta di Groq attraverso la sua API** ;
- è lo **standard de facto** per il riconoscimento vocale, è utilizzato in tutto il mondo e supporta un'ampia quantità di lingue con una buona qualità ;
- il **prezzo è molto competitivo** rispetto al mercato ;
- è **molto rapido**.

##### Whisper-large

In alternativa, nei parametri dell'estensione Whisper, potete scegliere il modello Whisper-Large-v3 che è :

- Leggermente più caro ;
- meno rapido ;
- Leggermente più preciso.


![[../assets/whisper_large_v3.png]]

#### Con Mistral

Attualmente, sul software IGOOR, **la migliore qualità di trascrizione**, almeno in francese, si ottiene con il modello **voxtral-mini-transcribe sviluppato da Mistral**. Potete utilizzarlo, con un prezzo a consumo, attraverso l'AI Studio di Mistral.

Se optate per Mistral, dovete quindi disporre di un account sull'AI Studio di Mistral. Se non lo avete ancora creato :

[[4 - Preferenze - IA]]

Una volta che avete una chiave API, andate in :

*Parametri > Home > Riconoscimento vocale > Configura il riconoscimento vocale*

![[../assets/reconnaissance_vocale.png]]


Nella pagina che si apre, scegliete Mistral invece di Groq come fornitore, e inserite la vostra chiave API Mistral.

![[../assets/voxtral_min.png]]
