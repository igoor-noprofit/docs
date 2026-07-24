Par défaut, **IGOOR déclenche la transcription au clic sur l'icône du micro, et l'arrête lors d'un deuxième clic**. Ce mécanisme a été conçu pour marquer avec clarté la voix à transcrire, et éviter des erreurs de transcription dans des environnements bruyants.

Vous pouvez utiliser un bouton externe pour que l'interlocuteur puisse déclencher et arrêter plus simplement la reconnaissance vocale, sans besoin de cliquer sur le PC de l'utilisateur et sans besoin d'action de la part de l'utilisateur.

![[../assets/asr_button.png]]

Si vous souhaitez acheter un [[2 - Bouton externe pour reconnaissance vocale]] :

**NOTE : Pour l'instant, le bouton externe fonctionne exclusivement quand la fenêtre d'IGOOR est active.**

## Mode d'écoute continue

Au lieu de cliquer sur le micro à chaque phrase, **depuis la v1 d'IGOOR vous pouvez choisir une écoute continue**. Dans cette modalité, vous cliquez une seule fois sur le micro pour démarrer la communication, et - à chaque fois que vous parlez - IGOOR transcrira vos phrases. Quand vous cliquez à nouveau sur le bouton, la conversation est terminée et l'écoute continue s'arrête. 

Vous pouvez activer l'écoute continue dans :

*Paramètres > Accueil > Configurer la reconnaissance vocale*

### Configurer l'écoute continue

L'écoute continue est une fonctionnalité qui peut nécessiter d'une personnalisation, qui se fait toujours dans :

*Paramètres > Accueil > Configurer la reconnaissance vocale*

Par ex., s'il y a un certain bruit ambiant de voix, vous pouvez monter le seuil de détection vocale. Si, en revanche, votre interlocuteur parle, mais la transcription ne se déclenche pas, essayez de le baisser.

**IMPORTANT : indépendamment de votre choix de système de reconnaissance vocale (locale ou cloud), les sons AVANT les débuts de la conversation restent à 100% sur votre ordinateur.** 

![[continuous_listening.png]]

Également, si IGOOR coupe trop souvent une phrase à cause des pauses que votre interlocuteur fait en parlant, vous pouvez monter la tolérance aux pauses. 

Si enfin vous souhaitez que les prédictions soient générées pour l'utilisateur en fonction de la sémantique de la conversation, vous pouvez décocher "Toujours générer des prédictions". IGOOR fera une analyse sémantique rapide pour décider si la phrase de votre interlocuteur est terminée ou pas, et donc si générer des prédictions ou attendre que l'interlocuteur termine.

## Mot de réveil

**Vous pouvez déclencher l'écoute continue non seulement avec le clic, mais aussi avec un mot de réveil. Le mot de réveil s'inspire des assistants vocaux comme Alexa, Siri** etc. : si vous dites "Hé, Igoor", IGOOR démarrera la conversation sans besoin d'aucun clic. 

**IMPORTANT : indépendamment de votre choix de système de reconnaissance vocale (locale ou cloud), la détection vocale est faite à 100% sur votre ordinateur. Si vous utilisez un fournisseur cloud, aucune données n'est envoyée au cloud tant que la conversation n'a pas démarré.** 

### Personnalisation du mot de réveil

Il est désormais possible, grâce au site [openwakeword.com](https://openwakeword.com/), de personnaliser facilement le mot de réveil. Au lieu de démarrer une conversation avec "Hé, Igoor" vous pouvez choisir d'autres mots, prénoms etc. dans votre langue, par ex. "Hé, Juliette" ou simplement "Juliette". Cette personnalisation nous semble fondamentale pour l'aspect humain.

**IMPORTANT : Nous ne sommes pas affiliés à Openwakeword.** 

Pour personnaliser le mot de réveil, vous pouvez choisir entre :

1) une librairie de mot de réveil à télécharger sur le site openwakeword (gratuit) ;
2) si le mot n'existe pas encore, vous pouvez entrainer un modèle spécifique (votre mot style "Alexa). Vous pouvez le faire seuls, sur le site openwakeword, mais l'association IGOOR peut vous accompagner sur cette procédure, qui n'est pas immédiate et est payante (quelques euros).

![[wakeword.png]]

#### Librairie de mots de réveil


### Configuration du mot de réveil

Au-delà du micro et de la distance de l'interlocuteur, la capacité d'IGOOR de détecter correctement le mot de réveil dépend de plusieurs aspects :

1) le modèle du mot ;
2) la longueur : "Hé, Juliette" est en général plus simple à détecter de "Juliette", mais une phrase trop longue est plus difficile ;
3) votre langue ;
4) la qualité de l'entrainement du modèle de mot de réveil.


