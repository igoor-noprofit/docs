Questa estensione aggiunge informazioni contestuali sul meteo (temperatura, vento etc.) al contesto, cioè all'insieme delle informazioni che vengono inviate all'IA per generare le previsioni (cf. [[1 - Quattro strumenti di aiuto alla comunicazione]]).

<div style="background:red;color:#fff; padding: 10px">
ATTENZIONE: per poter funzionare, il servizio deve recuperare la vostra posizione attuale ogni 10 minuti, basandosi sull'indirizzo IP della vostra connessione Internet. La precisione della posizione è variabile.
Questa estensione non è quindi utilizzabile offline.
</div>


## Attivazione dell'estensione

Andate in

*Parametri > Estensioni > Contesto > Weather :*

![[../assets/weather_activate.png]]

e attivate l'estensione tramite l'interruttore.

**PROMEMORIA : dovete riavviare IGOOR quando attivate (o disattivate) delle estensioni.**

## Configurazione dell'estensione

Andate in :

*Home > Gestione del meteo*

![[../assets/weather_activated.png]]

Cliccate sull'icona dei parametri dell'estensione.
L'estensione funziona grazie a un servizio gratuito fornito da https://open-meteo.com/ (a partire dalla versione 0.3.5.0), e non richiede abbonamento.

## Versioni precedenti

Le versioni precedenti richiedono di iscrivervi e recuperare la vostra chiave API qui :

[Ottenere una chiave API gratuita Openweathermap](https://home.openweathermap.org/users/sign_up){target: blank}


![[../assets/weather_config.png]]

## Indirizzo di casa

Potete inserire l'indirizzo esatto della vostra abitazione. **Questo indirizzo non viene mai comunicato all'esterno ; è utilizzato all'interno di IGOOR per confrontarlo con quello aggiornato automaticamente, al fine di capire se l'utente è a casa.**

Salvate le vostre modifiche.
## Verifica

Una volta che avete attivato il meteo, vedrete la temperatura nella barra in alto :

![[../assets/weather_icon_topbar.png]]

Da questo momento, le informazioni sul meteo vengono aggiunte alle previsioni delle frasi.
