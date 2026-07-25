### A partire dalla v1 di IGOOR :

- Selezionate semplicemente il modello **Sherpa-ONNX (locale)** come fornitore.
- Selezionate la taglia grande (consigliata per la qualità) o la taglia piccola (solo se la trascrizione è troppo lenta)

Quando salvate i parametri, se è la prima volta che utilizzate il modello locale, IGOOR scaricherà sul vostro computer il modello. Questo può richiedere alcuni minuti. Non è necessario riavviare.

---
### Per le versioni precedenti alla v1 :

Andate in :

*Parametri > Estensioni > ASR*

- disattivate il modulo ASR JAVASCRIPT
- attivate il modulo VOSK
- salvate i parametri globali

Riavviate IGOOR.

Il riconoscimento vocale di Vosk richiede una quantità di memoria (RAM) che arriva a 3 GB per il modello di grande taglia. Potete cambiare la dimensione del modello nei parametri del plugin Vosk se la vostra memoria non è sufficiente.

**IMPORTANTE : l'estensione VOSK è stata sostituita dal modello Sherpa-ONNX nella versione 1, e non sarà più supportata.**
