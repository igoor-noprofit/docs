La reconnaissance vocale (ou ASR, automatic-speech-recognition) permet aujourd'hui de pouvoir **inclure l'interlocuteur** dans le processus de dialogue avec l'utilisateur, au lieu d'attendre toujours l'initiative de communication de l'utilisateur.

La reconnaissance vocale par défaut se base sur l'IA de Groq, mais vous pouvez modifier votre fournisseur dans :

Paramètres > Accueil > Reconnaissance vocale > Configurer la reconnaissance vocale 

**IMPORTANT : Actuellement, nous utilisons un bouton externe pour que l'interlocuteur puisse déclencher plus simplement la reconnaissance vocale, sans besoin d'action par l'utilisateur ; mais également pour éviter des bruits parasites, notamment dans des environnements très bruyants.**

Si vous ne disposez pas de bouton externe, cliquez sur l'icône du micro dans le logiciel IGOOR pour faire partir la reconnaissance vocale, et cliquez à nouveau pour la faire arrêter :

![[../assets/asr_button.png]]
Le bouton déclenche la transcription des mots de l'interlocuteur.
Cf. [[2 - Bouton externe pour reconnaissance vocale]] 

## L'IA transcrit votre phrase, "raisonne" et génère des prédictions

### TRANSCRIPTION

Le choix de votre modèle de reconnaissance vocale (voir [[Local or cloud ASR]]) peut affecter la qualité de la transcription. Cependant, les modèles de langage arrivent souvent à dépasser les "hallucinations" de transcription en utilisant le contexte, par ex. la conversation en cours.

Voici un exemple de phrase prononcée par l'interlocuteur, transcrite par l'I.A. :

![[asr_transcription.png]]

### RAISONNEMENT

**L'I.A. "raisonne" avant de générer les réponses**. Ce processus, invisible pour l'utilisateur, est cependant important pour comprendre comment elle fonctionne, et le fait qu'elle prend en considération les préférences de l'utilisateur (dans ce cas, les préférences alimentaires) :

`We need to consider Igor's preferences: prefers fish, soups, light, soft foods, dislikes heavy, likes fish, likes miso, foie gras? He likes foie de veau, foie de morue, but not heavy? He likes fish, soups, light, avoids heavy meat. He also has difficulty chewing and swallowing, prefers soft foods, fish, soups, non-spicy Asian soups. He doesn't like rice cake. So for options: fish (good), foie gras (maybe heavy and rich, but could be okay?), meat (likely heavy, not preferred), spaghettis (hard to chew, not ideal), fruits (soft, okay). So we can give positive responses for fish and maybe fruits, neutral for foie gras, negative for meat and spaghettis. Need between 3 and 6 answers total, spread across columns: left (positive), center (mitigated/alternative/ironic), right (negative). Left can have 1-2 answers, center 1-2, right 1-2. Must have at least 3 total. Provide up to 6.` `We also need to incorporate Igor's ironic style at most 1 in 6. So maybe one answer is ironic, placed maybe in center.`

**NOTE : Le raisonnement n'est pas supporté sur tous les modèles.** Le raisonnement peut également rendre le temps de génération de réponses légèrement plus long, mais améliore en général la qualité des prédictions.

### GENERATION ET AFFICHAGE DES REPONSES

**Les réponses sont ensuite structurées visuellement sur trois colonnes :**

![[../assets/flow_3_cols.png]]

**Le principe est le même que sur les besoins quotidiens :**

- **À gauche, nous avons des réponses "positives"** (dans ce cas, l'acceptation de poisson ou du bouillon de poisson) ;
- **À droite, nous avons des réponses "négatives"** (dans ce cas, des aliments qu'il refuse) ;
- **Au centre, nous avons deux réponses plus nuancées**.

Plusieurs phrases peuvent être clickées, et donc prononcées à travers la synthèse vocale, l'une après l'autre : dans ce cas spécifique, l'utilisateur pourrait en choisir plusieurs pour indiquer toutes ses préférences pour le repas.

## ASTUCES POUR LES UTILISATEUR
- **Clicker à nouveau sur la phrase, une fois qu'elle est insérée dans la conversation, engendre la répétition de la phrase** ; utile si l'autre personne n'a pas bien entendu, ou en cas d'erreur de génération

## ASTUCES POUR LES INTERLOCUTEURS

- **Utilisez des phrases simples**
- Parlez avec une **élocution claire**
- Fournissez une **information la plus complète possible, pour aider l'IA à mieux situer le contexte**