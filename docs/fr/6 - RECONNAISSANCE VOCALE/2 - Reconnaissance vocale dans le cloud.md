#### Avec Groq
##### Whisper-large-v3-turbo

**Ce modèle fourni par Groq est le modèle par défaut d'IGOOR parce que :**

- **Déjà intégrée à l'offre de Groq à travers son API** ;
- c'est le **standard de facto** pour la reconnaissance vocale, il est utilisé partout dans le monde et supporte une large quantité de langues avec une bonne qualité ;
- le **prix est très compétitif** par rapport au marché ;
- il est **très rapide**.

##### Whisper-large

En alternative, dans les paramètres de l'extension Whisper, vous pouvez choisir le modèle Whisper-Large-v3 qui est :

- Légèrement plus cher ;
- moins rapide ;
- Légèrement plus précis. 


![[../assets/whisper_large_v3.png]]

#### Avec Mistral

Actuellement, sur le logiciel IGOOR, **la meilleure qualité de transcription**, du moins en français, s'obtient avec le modèle **voxtral-mini-transcribe développé par Mistral**. Vous pouvez l'utiliser, avec un prix à la consommation, à travers le AI Studio de Mistral. 

Si vous optez pour Mistral, vous devez donc disposer d'un compte sur le AI Studio de Mistral. Si vous ne l'avez pas déjà créé :

[[4 - Préférences - IA]]

Une fois que vous avez une clé API, allez dans :

*Paramètres > Accueil > Reconnaissance Vocale > Configurer la reconnaissance vocale*

![[../assets/reconnaissance_vocale.png]]


Dans la page qui s'ouvre, choisissez Mistral au lieu de Groq comme fournisseur, et insérez votre clé API Mistral.

![[../assets/voxtral_min.png]]
