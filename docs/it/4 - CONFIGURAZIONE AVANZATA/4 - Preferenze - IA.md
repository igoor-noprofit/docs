**A partire dalla versione 1, IGOOR supporta diversi fornitori cloud di IA**, oltre alla possibilità di usare la vostra IA locale.

## Comparativa dei fornitori cloud di IA

Ecco un comparativo dei fornitori cloud per aiutarvi a scegliere:

| CARATTERISTICHE / FORNITORE                                                | GROQ<br>                                                    | MISTRAL                                                              | CEREBRAS                                                                                    |
| -------------------------------------------------------------------------- | ----------------------------------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| velocità                                                                   | molto buona                                                 | molto buona sul loro modello piccolo                                 | eccellente, in particolare sui prompt più lunghi                                            |
| prezzo                                                                     | gratuito entro i limiti di utilizzo o prezzo a consumo      | gratuito entro i limiti di utilizzo o prezzo a consumo                | gratuito entro i 5$ di consumo offerti, automaticamente a pagamento a consumo dopo          |
| rapporto velocità / prezzo                                                 | migliore                                                    | dipendente dal modello                                               | secondo migliore                                                                            |
| possibilità di usare il fornitore senza inserire i dati di pagamento       | ✅                                                           | ✅                                                                    | ❌                                                                                           |
| offre un modello di riconoscimento vocale                                  | ✅                                                           | ✅                                                                    | ❌                                                                                           |
| modelli *open-source*                                                      | ✅                                                           | ❌                                                                    | ✅                                                                                           |
| i vostri dati NON sono usati per addestrare il modello                     | ✅                                                           | *opt-out* nell'offerta gratuita: dovete specificare la vostra preferenza | ✅                                                                                           |
| server in Europa                                                           | ✅                                                           | ✅                                                                    | entro fine 2026                                                                             |
| rispetto della privacy                                                     | molto buono                                                 | *opt-out* opzionale                                                  | buono                                                                                       |

Per Groq, vi rimandiamo alla [[2 - Configurazione rapida]].

### Usare IGOOR gratuitamente con Mistral

Come Groq, anche Mistral offre i suoi modelli di previsione testuali, oltre a un ottimo modello di riconoscimento vocale.
Ci sono due differenze principali rispetto a Groq:

1) i suoi modelli non sono open-source né open-weights: tuttavia, tutta la loro infrastruttura è in Francia e quindi deve rispettare il RGPD francese, che è molto rigoroso. Verificate la loro [informativa sulla privacy](https://legal.mistral.ai/terms/privacy-policy?language=fr-FR 
2) i loro modelli più grandi non sono altrettanto rapidi dei modelli grandi di Groq

Il processo per ottenere una chiave Mistral è simile a quello di Groq.
Andate su:

[Ottenere una chiave API gratuita Mistral](https://console.mistral.ai/)
![[../assets/console_mistral.png]]
Iscrivetevi, e cliccate poi su *Chiavi API* dal menu a sinistra:

![[../assets/mistral_api_key.png]]

Cliccate poi su *Aggiungi una nuova chiave*:

![[../assets/generate_api_key_mistral.png]]

Date un nome alla chiave e cliccate su *Nuova chiave*.

![[../assets/create_key_mistral.png]]

Potete creare quante chiavi API desiderate, ma non potete visualizzarle una seconda volta. Cliccate su *Copia*:

![[../assets/copy_mistral_key.png]]

Tornate nel software IGOOR, entrate nei parametri (pulsante in alto a destra) e cliccate sulla scheda IA.

![Incolla la chiave](../assets/paste_api_key.png)

Selezionate Mistral come fornitore, e incollate poi la chiave nel campo Chiave API. Cliccate poi sul pulsante *Salva impostazioni principali*.

Se desiderate usare Mistral anche per il riconoscimento vocale nel cloud, dovete specificarlo manualmente. Vedere [[2 - Riconoscimento vocale nel cloud]]


### Provare IGOOR gratuitamente con Cerebras

Da notare che:

- **A partire dal 17 luglio 2026, per provare gratuitamente Cerebras entro il limite di 5$ di credito, dovete inserire i vostri dati di pagamento**. Oltre i 5$ di consumo, pagherete automaticamente a consumo.
- Inoltre, **Cerebras non offre un modello di riconoscimento vocale nel cloud**. Di conseguenza, se optate per un riconoscimento vocale nel cloud, dovrete usare Groq o Mistral.

**Consigliamo quindi Cerebras esclusivamente agli utenti più avanzati.**
