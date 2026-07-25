## Installazione dell'applicazione

### Smart Screen

L'associazione IGOOR non è ancora certificata come editore di software. SmartScreen potrebbe quindi non permettervi di avviare affatto il processo di installazione e mostrarvi questo popup:

![Smart screen](https://learn-attachment.microsoft.com/api/attachments/fcf98b41-6f23-4eef-999f-7c9c6f212ce0?platform=QnA)

**SOLUZIONE: Cliccare su "Ulteriori informazioni" e poi su "Esegui comunque"**

### Antivirus

Al termine del processo di installazione, l'avvio dell'applicazione può fallire a causa di un falso positivo nel rilevamento di virus da parte di Windows o del vostro antivirus. Si apre un popup che vi informa che l'applicazione è stata riconosciuta come un virus.

**SOLUZIONE: Eseguite l'installazione del software come amministratore** cliccando sull'icona dell'applicazione con il pulsante destro del mouse e selezionando «Esegui come amministratore» nella finestra contestuale che si apre.

![Smart screen](../assets/run_as_administrator.png)


## Utilizzo dell'applicazione

### Visualizzazione errata nell'applicazione

Se la schermata dei bisogni quotidiani appare così:

![[../assets/bug_windows_font_size.png]]

Molto probabilmente dipende da un ridimensionamento del testo operato automaticamente da Windows.

Seguite questa procedura su Windows:

Andate in:

**Start > Impostazioni > Sistema > Schermo**

Scorrete fino alla sezione **Scala e disposizione**.

Se la percentuale è superiore al 100%-150%, impostandola al 100% (e riavviando IGOOR) la visualizzazione dovrebbe correggersi.

### Le previsioni non appaiono

Avete una chiave dell'API di Groq a pagamento?
Se non è il caso, esiste una limitazione della frequenza e della lunghezza delle richieste (al minuto e al giorno) che può impattare sull'utilizzo dell'applicazione.

### Il riconoscimento vocale è di bassa qualità

I modelli di riconoscimento vocale attuali non sono perfetti.
Seguite i consigli in [[2 - Dialogo con l'interlocutore]].
Inoltre:

1) Un buon microfono (e una buona distanza tra l'interlocutore e il microfono) possono migliorare enormemente la qualità;
2) Se utilizzate il modello locale, assicuratevi di usare la sua taglia large;
3) Se utilizzate il modello cloud di Groq, provate a passare a Whisper-Large in versione non turbo in [[2 - Riconoscimento vocale nel cloud]]