## Configurazione hardware

- PC o tablet **Windows 10/11**
- **Risoluzione minima: 1280x960**
- Risoluzione consigliata: 1920x1080 (Full HD) o superiore
- **Memoria RAM consigliata: 16 GB o più**

## Configurazione rapida: funzionamento nel cloud

Il modo più semplice e rapido per usare IGOOR è affidarsi ai servizi gratuiti di Groq, un provider cloud di IA e di riconoscimento vocale. 
Avrete bisogno soltanto di:

- **Una connessione internet** (preferibilmente fibra ottica o ADSL)
- **Una chiave API Groq (gratuita o a pagamento)**

NOTA: a partire dalla versione 1, IGOOR supporta anche altri provider, come il francese Mistral (per IA / riconoscimento vocale) e Cerebras (solo IA). Vedi [[4 - Preferenze - IA]]

### Come ottenere una chiave API gratuita Groq

Potete richiedere una chiave sviluppatore ("*developer*") a Groq, provider cloud di inferenza IA.

[Ottieni una :key: Groq](https://console.groq.com/keys){ .md-button target=_blank}

**IMPORTANTE: non siamo né partner né affiliati di Groq.**

### Prerequisiti per un funzionamento 100% locale

**NOTA: a partire dalla versione 1 di IGOOR, non avete più bisogno di Internet se usate tutte le opzioni locali per i diversi servizi.** La connessione Internet sarà tuttavia necessaria in fase di attivazione delle varie opzioni.

Il funzionamento 100% locale implica:

1) Installare, sul vostro PC, un modello di linguaggio di grandi dimensioni (LLM) che metta a disposizione un endpoint compatibile con OpenAI. **Oggi, questo richiede un PC estremamente potente per ottenere una qualità e una velocità di previsione paragonabili alle soluzioni cloud.**
2) Usare il modello Sherpa-ONNX per il riconoscimento vocale in locale (vedi [[2 - Riconoscimento vocale nel cloud]])
3) Mantenere la voce di sintesi Windows (vedi [[1 - Scegliere il sistema di sintesi vocale TTS]])
