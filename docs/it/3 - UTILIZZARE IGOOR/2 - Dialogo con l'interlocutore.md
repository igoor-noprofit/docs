## Breve storia dell'interlocutore nei software di CAA

**Tradizionalmente, i software di CAA hanno sempre tenuto conto esclusivamente della volontà di comunicare da parte dell'utente**.

**La grande novità introdotta da IGOOR**, resa possibile dall'intelligenza artificiale generativa e dal riconoscimento vocale, consiste nel **trascrivere la voce dell'interlocutore** per arricchire il contesto della conversazione e generare previsioni. Ciò **include l'interlocutore** nel processo di dialogo con l'utente, invece di attendere sempre l'iniziativa comunicativa dell'utente.

<div style="background:#666;color:#fff; padding: 10px"><strong>NOTA : per quanto ci consta, siamo stati i primi a proporre questo concetto e a realizzarlo</strong>, fin dal nostro prototipo di validazione, che mostravamo già <strong>nel giugno 2024 </strong><a style="color:#fff" target="blank" href="https://vimeo.com/969643455">in questo video su Vimeo</a>.
<br><strong>Se siamo così fieri di averlo fatto, è anche perché questa idea nasce da Igor Novitzki, fondatore della nostra associazione, anch'egli colpito dalla SLA.</strong></div>

## Il riconoscimento vocale (ASR)

Il riconoscimento vocale (ASR, *Automated Speech Recognition*) predefinito si basa sull'IA di Groq, ma potete modificare il vostro fornitore in :

*Parametri > Home > Riconoscimento vocale > Configura il riconoscimento vocale*

Esistono inoltre diversi modi per attivare la trascrizione della voce dell'interlocutore (cf. [[1 - Riconoscimento vocale]]).

Per impostazione predefinita, il clic sull'icona del microfono attiva la trascrizione delle parole dell'interlocutore, e

## L'IA trascrive la vostra frase, "ragiona" e genera previsioni

### TRASCRIZIONE

La scelta del modello di riconoscimento vocale può influire sulla qualità della trascrizione. Tuttavia, i modelli di linguaggio riescono spesso a superare le "allucinazioni" di trascrizione sfruttando il contesto, ad es. la conversazione in corso.

Ecco un esempio di frase pronunciata dall'interlocutore, trascritta dall'I.A. :

![[asr_transcription.png]]

### RAGIONAMENTO

**L'I.A. "ragiona" prima di generare le risposte**. Questo processo, invisibile per l'utente, è tuttavia importante per capire come funziona e il fatto che tenga in considerazione le preferenze dell'utente (in questo caso, le preferenze alimentari) :

`We need to consider Igor's preferences: prefers fish, soups, light, soft foods, dislikes heavy, likes fish, likes miso, foie gras? He likes foie de veau, foie de morue, but not heavy? He likes fish, soups, light, avoids heavy meat. He also has difficulty chewing and swallowing, prefers soft foods, fish, soups, non-spicy Asian soups. He doesn't like rice cake. So for options: fish (good), foie gras (maybe heavy and rich, but could be okay?), meat (likely heavy, not preferred), spaghettis (hard to chew, not ideal), fruits (soft, okay). So we can give positive responses for fish and maybe fruits, neutral for foie gras, negative for meat and spaghettis. Need between 3 and 6 answers total, spread across columns: left (positive), center (mitigated/alternative/ironic), right (negative). Left can have 1-2 answers, center 1-2, right 1-2. Must have at least 3 total. Provide up to 6.` `We also need to incorporate Igor's ironic style at most 1 in 6. So maybe one answer is ironic, placed maybe in center.`

**NOTA : Il ragionamento non è supportato su tutti i modelli.** Il ragionamento può inoltre rendere leggermente più lungo il tempo di generazione delle risposte, ma in generale migliora la qualità delle previsioni.

### GENERAZIONE E VISUALIZZAZIONE DELLE RISPOSTE

**Le risposte vengono quindi strutturate visivamente su tre colonne :**

![[../assets/flow_3_cols.png]]

**Il principio è lo stesso dei bisogni quotidiani :**

- **A sinistra troviamo risposte "positive"** (in questo caso, l'accettazione del pesce o del brodo di pesce) ;
- **A destra troviamo risposte "negative"** (in questo caso, cibi che rifiuta) ;
- **Al centro troviamo due risposte più sfumate**.

Più frasi possono essere cliccate e quindi pronunciate tramite la sintesi vocale, l'una dopo l'altra : in questo caso specifico, l'utente potrebbe sceglierne diverse per indicare tutte le proprie preferenze per il pasto.

## CONSIGLI PER GLI UTENTI

- **Cliccare nuovamente sulla frase, una volta inserita nella conversazione, ne provoca la ripetizione** ; utile se l'altra persona non ha sentito bene, o in caso di errore della sintesi vocale.

## CONSIGLI PER GLI INTERLOCUTORI

- **Usate frasi semplici**
- Parlate con una **dizione chiara**
- Fornite **un'informazione il più completa possibile, per aiutare l'IA a inquadrare meglio il contesto**
