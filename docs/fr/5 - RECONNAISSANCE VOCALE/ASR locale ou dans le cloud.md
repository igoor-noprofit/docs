En fonction des possibilités techniques de votre dispositif, de la performance que vous souhaitez obtenir et du budget que vous souhaitez dépenser, vous pouvez opter pour une reconnaissance vocale (ASR, *Automated Speech Recognition*) sur votre dispositif (avec le modèle Vosk) ou dans le cloud.

## ASR dans le cloud

### Mistral

Actuellement, sur le logiciel IGOOR, **la meilleure qualité de transcription**, notamment en français, s'obtient avec le modèle **voxtral-mini-transcribe développé par Mistral**. Vous pouvez l'utiliser, avec un prix à la consommation, à travers le AI Studio de Mistral. 

Si vous optez pour Mistral, vous devez donc créer un compte sur le AI Studio de Mistral : 

![[../assets/Pasted image 20251211105340.png]]

[S'abonner à Mistral et créer une clé API](https://docs.mistral.ai/getting-started/quickstart)

Une fois que vous obtenez une clé API, allez dans :

Paramètres > Extensions > ASR JAVASCRIPT

Et cliquez sur l'icône des paramètres de l'extension Whisper.

Choisissez Mistral au lieu de Groq comme fournisseur, et insérez votre clé API. 

### Whisper

**La deuxième meilleure option supportée par IGOOR est Whisper-large-v3, fourni par Groq.** C'est l'option par défaut parce que :

- Déjà intégrée à l'offre de Groq à travers son API ;
- ce modèle est le standard de facto pour la reconnaissance vocale, il est amplement utilisé partout dans le monde et supporte une large quantité de langues avec une qualité suffisante ;
- le prix est très compétitif par rapport au marché.

En alternative, dans les paramètres de l'extension Whisper, vous pouvez choisir le modèle Whisper Large v3 Turbo qui est :

- moins cher
- plus rapide
- moins précis.

![[../assets/Pasted image 20251211105416.png]]

## ASR local

Allez dans :

Paramètres > Extensions > ASR 

- désactivez le module ASR JAVASCRIPT
- activez le module VOSK

Rédemarrez IGOOR.

VOSK est réservé à l'usage en local, pour ceux qui ne souhaitent pas payer pour un service de reconnaissance vocale ou pour des raisons de confidentialité.

**La reconnaissance vocale locale demande une quantité de mémoire vive (RAM) qui atteint les 3Go pour le modèle de grande taille. Vous pouvez changer la taille du modèle dans les paramètres du plugin Vosk si votre mémoire vive n'est pas suffisante.**


