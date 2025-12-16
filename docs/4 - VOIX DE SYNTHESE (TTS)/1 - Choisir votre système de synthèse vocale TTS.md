
## Synthèses vocales supportées

IGOOR supporte 3 modalités de TTS (Text-to-speech) :

1. Le **TTS intégré à Windows** (TTSDEFAULT)
2. **Elevenlabs**, un des acteurs majeurs dans le domaine de la synthèse vocale 
3. **Speechify**

D'autres fournisseurs pourront etre supportés à l'avenir. 

| CARACTERISTIQUES / PLUGIN                  | TTSDEFAULT<br>   | SPEECHIFY<br>                                                | ELEVENLABS<br>                                                                                                       |
| ------------------------------------------ | ---------------- | ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| fonctionne hors-connexion                  | ✅                | ❌                                                            | ❌                                                                                                                    |
| prix                                       | Gratuit          | [prix à la consommation](https://speechify.com/pricing-api/) | [prix à la consommation](https://elevenlabs.io/)<br><br>Le clone professionnel nécessite d'un abonnement mensuel pro |
| quantité de minutes gratuit                | Toujours gratuit | 100                                                          | 10                                                                                                                   |
| clone de voix professionnel                | ❌                | ❌                                                            | ✅                                                                                                                    |
| qualité de la voix                         | standard         | très bonne                                                   | très bonne, et excellente sur un clonage professionnel                                                               |
| changement d'intonation sur la meme phrase | ❌                | ✅                                                            | ✅                                                                                                                    |

**IMPORTANT: L'association loi 1901 IGOOR n'est pas affilié avec Speechify ou Elevenlabs.**

### Conseils

- **Si l'utilisateur d'IGOOR est affecté par la SLA, l'association ARSLA dispose de licences gratuites pour Elevenlabs**. [Contacter l'association ARSLA](https://www.arsla.org/)
- Si vous avez la possibilité de [[2 - Cloner la voix de l'utilisateur d'IGOOR]], nous vous conseillons
- Seulement si vous n'avez pas la possibilité de cloner la voix de l'utilisateur, ou que vous souhaitez une voix gratuite, choisissez le TTSDEFAULT. **La voix originale de la personne (ou une voix plus expressive des voix Windows) contribuent à garder un lien émotionnel avec l'utilisateur.**

## Utiliser la voix de synthèse fournie par Windows

Allez dans : 

Paramètres > Extensions > TTS

Clic sur l'icône des paramètres de l'extension *Default Text-to-speech* : 

![[Pasted image 20251118161524.png]]

Décochez la case pour utiliser **toujours** la voix de Windows.
Choisissez la voix que vous souhaitez dans le menu déroulant et enregistrez les paramètres du plugin.

## Utiliser une voix de synthèse dans le cloud

**IMPORTANT : Nous vous conseillons de garder activée la voix de synthèse Windows comme fallback (en cas de problèmes réseau).**
Pour ce faire, dans les paramètres de l'extension ci-dessus, gardez la case cochée. Ensuite, activez l'extension correspondante à votre abonnement (Elevenlabs ou Speechify).

Vous allez devoir ensuite **renseigner votre clé API** pour l'accès au service. Par exemple pour Speechify :

![[Pasted image 20251118163635.png]]

Une fois la clé API renseigné, la liste des voix disponibles se remplira.
Ensuite, en fonction de votre abonnement, vous allez pouvoir choisir une voix spécifique (votre voix clonée, ou une autre voix) et en personnaliser quelques paramètres :

![[Pasted image 20251118163754.png]]






