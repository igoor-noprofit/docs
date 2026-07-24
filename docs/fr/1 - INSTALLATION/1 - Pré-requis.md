## Configuration matérielle

- PC ou tablette **Windows 10/11**
- **Résolution minimale : 1280x960**
- Résolution conseillée : 1920x1080 (Full HD) ou supérieure
- **Mémoire vive conseillée : 16 Go ou plus**

## Configuration rapide : fonctionnement dans le cloud

Le moyen le plus simple et rapide d'utiliser IGOOR est en s'appuyant sur les services gratuit de Groq, un fournisseur cloud d'IA et de reconnaissance vocale. 
Vous aurez besoin seulement de :

- **Une connexion internet** (de préférence fibre optique ou ADSL)
- **Une clé API Groq (gratuite ou payante)**

NOTE : À partir de la version 1, IGOOR supporte également autres fournisseurs, comme le français Mistral (pour IA / reconnaissance vocale) et Cerebras (IA seulement). Voir [[4 - Préférences - IA]]

### Comment obtenir une clé API gratuite Groq

Vous pouvez demander une clé développeur ("*developer*") à Groq, fournisseur cloud d'inference IA.

[Obtenir une :key: Groq](https://console.groq.com/keys){ .md-button target=_blank}

**IMPORTANT: Nous ne sommes ni partenaires ni affiliés de Groq.**

### Pré-requis pour un fonctionnement 100% local

**NOTE: A partir de la version 1 d'IGOOR, vous n'avez plus besoin d'Internet si vous utilisez toutes les options locales pour les différents services.** La connexion Internet sera cependant nécessaire lors de l'activation des différents options.

Le fonctionnement 100% local implique :

1) Installer, sur votre PC, un modèle de langage large (LLM) qui met à disposition un endpoint compatible avec OpenAI. **Aujourd'hui, cela demande un PC extremement puissant pour obtenir une qualité et vitesse des prédictions comparable avec les solutions cloud.**
2) Utiliser le modèle Sherpa-ONNX pour la reconnaissance vocale en locale (cf. [[2 - Reconnaissance vocale dans le cloud]])
3) Garder la voix de synthèse Windows (cf. [[1 - Choisir votre système de synthèse vocale TTS]])

