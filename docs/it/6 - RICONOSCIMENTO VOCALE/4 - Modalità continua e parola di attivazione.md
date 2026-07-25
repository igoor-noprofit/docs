Per impostazione predefinita, **IGOOR avvia la trascrizione al clic sull'icona del microfono, e la interrompe con un secondo clic**. Questo meccanismo è stato pensato per delimitare chiaramente la voce da trascrivere, ed evitare errori di trascrizione in ambienti rumorosi.

Potete utilizzare un pulsante esterno per consentire all'interlocutore di avviare e interrompere più semplicemente il riconoscimento vocale, senza bisogno di cliccare sul PC dell'utente e senza alcuna azione da parte dell'utente.

![[../assets/asr_button.png]]

Se desiderate acquistare un [[2 - Pulsante esterno per il riconoscimento vocale]] :

**NOTA : per il momento, il pulsante esterno funziona esclusivamente quando la finestra di IGOOR è attiva.**

## Modalità di ascolto continuo

Invece di cliccare sul microfono a ogni frase, **a partire dalla v1 di IGOOR potete scegliere un ascolto continuo**. In questa modalità, cliccate una sola volta sul microfono per avviare la comunicazione, e - ogni volta che parlate - IGOOR trascriverà le vostre frasi. Quando cliccate nuovamente sul pulsante, la conversazione è terminata e l'ascolto continuo si interrompe.

Potete attivare l'ascolto continuo in :

*Parametri > Home > Configura il riconoscimento vocale*

### Configurare l'ascolto continuo

L'ascolto continuo è una funzionalità che può richiedere una personalizzazione, che si effettua sempre in :

*Parametri > Home > Configura il riconoscimento vocale*

Ad es., se c'è un certo rumore ambientale di voci, potete alzare la soglia di rilevamento vocale. Se invece il vostro interlocutore parla, ma la trascrizione non si avvia, provate ad abbassarla.

**IMPORTANTE : indipendentemente dalla vostra scelta del sistema di riconoscimento vocale (locale o cloud), i suoni PRIMA dell'inizio della conversazione restano al 100% sul vostro computer.**

![[continuous_listening.png]]

Inoltre, se IGOOR interrompe troppo spesso una frase a causa delle pause che il vostro interlocutore fa parlando, potete aumentare la tolleranza alle pause.

Infine, se desiderate che le previsioni siano generate per l'utente in funzione della semantica della conversazione, potete deselezionare "Genera sempre le previsioni". IGOOR effettuerà una rapida analisi semantica per decidere se la frase del vostro interlocutore è terminata o no, e quindi se generare le previsioni o aspettare che l'interlocutore finisca.

## Parola di attivazione

**Potete attivare l'ascolto continuo non solo con il clic, ma anche con una parola di attivazione. La parola di attivazione si ispira agli assistenti vocali come Alexa, Siri** ecc. : se dite "Ehi, Igoor", IGOOR avvierà la conversazione senza bisogno di alcun clic.

**IMPORTANTE : indipendentemente dalla vostra scelta del sistema di riconoscimento vocale (locale o cloud), il rilevamento vocale viene effettuato al 100% sul vostro computer. Se utilizzate un fornitore cloud, nessun dato viene inviato al cloud finché la conversazione non è iniziata.**

### Personalizzazione della parola di attivazione

È ormai possibile, grazie al sito [openwakeword.com](https://openwakeword.com/), personalizzare facilmente la parola di attivazione. Invece di avviare una conversazione con "Ehi, Igoor" potete scegliere altre parole, nomi ecc. nella vostra lingua, ad es. "Ehi, Giulietta" o semplicemente "Giulietta". Questa personalizzazione ci sembra fondamentale per l'aspetto umano.

**IMPORTANTE : Non siamo affiliati a Openwakeword.**

Per personalizzare la parola di attivazione, potete scegliere tra :

1) una libreria di parole di attivazione da scaricare sul sito openwakeword (gratuita) ;
2) se la parola non esiste ancora, potete addestrare un modello specifico (la vostra parola in stile "Alexa"). Potete farlo da soli, sul sito openwakeword, ma l'associazione IGOOR può accompagnarvi in questa procedura, che non è immediata ed è a pagamento (qualche euro).

![[wakeword.png]]

#### Libreria di parole di attivazione


### Configurazione della parola di attivazione

Oltre al microfono e alla distanza dell'interlocutore, la capacità di IGOOR di rilevare correttamente la parola di attivazione dipende da diversi aspetti :

1) il modello della parola ;
2) la lunghezza : "Ehi, Giulietta" è in generale più semplice da rilevare di "Giulietta", ma una frase troppo lunga è più difficile ;
3) la vostra lingua ;
4) la qualità dell'addestramento del modello di parola di attivazione.

