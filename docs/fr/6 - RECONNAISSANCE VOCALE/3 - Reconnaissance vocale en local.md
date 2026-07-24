### A partir de la v1 d'IGOOR :

- Sélectionnez simplement le modèle **Sherpa-ONNX (local)** en tant que fournisseur.
- Sélectionnez la taille large (conseillé pour la qualité) ou la taille petite (seulement si la transcription est trop lente)

Quand vous sauvegardez les paramètres, si c'est la première fois que vous utilisez le modèle local, IGOOR téléchargera sur votre ordinateur le modèle. Cela peut prendre quelques minutes. Vous n'avez pas besoin de redémarrer.

--- 
### Pour les versions précédentes à la v1 :

Allez dans :

*Paramètres > Extensions > ASR*

- désactivez le module ASR JAVASCRIPT
- activez le module VOSK
- enregistrez les paramètres globaux

Redémarrez IGOOR.

La reconnaissance vocale de Vosk demande une quantité de mémoire vive (RAM) qui atteint les 3Go pour le modèle de grande taille. Vous pouvez changer la taille du modèle dans les paramètres du plugin Vosk si votre mémoire vive n'est pas suffisante.

**IMPORTANT : l'extension VOSK a été remplacée par le modèle Sherpa-ONNX dans la version 1, et elle ne sera plus supportée.**