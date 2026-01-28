Vous pouvez extraire automatiquement des informations sur vous, venant de documents contenant informations significatives sur votre vie. 

IGOOR accepte les formats suivants :

- **PDF** (extension .pdf)
- **Texte** (extension .txt)
- **Markdown** (extension .md)

D'autres formats pourraient être ajoutés dans les versions futures. 

## Outil web d'enregistrement de la mémoire biographique

Au départ, **en dehors des informations obligatoires sur votre prénom, état de santé etc., IGOOR n'a aucune information sur vous** : il est donc difficile pour IGOOR de comprendre les relations d'amitié, de parenté et plein d'autres informations sur vous. 

Nous pouvons vous accompagner sur la création d'un document rempli de ce genre d'informations significatives à travers un formulaire web que vous pouvez remplir soit avec votre voix (transcrite automatiquement), soit en utilisant le clavier.

Pour en savoir plus sur cette procédure :

[Comment accéder à l'outil web d'enregistrement de la mémoire biographique](https://igoor.org/enregistreur-vocal/){target=blank}
## Intégration de documents

Dans cette version beta, **vous devez manuellement déplacer les documents que vous souhaitez intégrer dans un dossier spécifique** pour que l'application, au prochain lancement, les intègre à la mémoire. 
IGOOR crée un dossier sur votre ordinateur au premier lancement, dans C:\Utilisateurs ou C:\Users. Si votre nom utilisateur est Pierre, par exemple, vous allez devoir mettre vos documents dans :

C:\Users\pierre\AppData\Roaming\igoor\plugins\rag\medias

ou 

C:\Utilisateurs\pierre\AppData\Roaming\igoor\plugins\rag\medias

L'application garde trace des documents que vous avez déjà intégrés à la mémoire. Si à l'avenir vous souhaitez ajouter d'autres documents, il suffira de les déplacer dans le dossier. 
L'intégration se fait au prochain lancement de l'application IGOOR. 

## Conseils

L'IA fera de son mieux pour "comprendre" les informations dans vos documents. 
Idéalement, il est conseillé néanmoins d'utiliser dans vos textes des répétitions fréquentes du sujet pour éviter des problèmes d'attribution, par exemple : 

%% Pierre est le beau-fils de Jean-Marc. La femme de Jean-Marc s'appelle Julie. Julie et Jean-Marc habitent à Nancy.  %%

Pour tester que IGOOR prenne bien en compte vos prédictions, vous pouvez par ex. utiliser la complétion automatique. Dans l'exemple ci-dessus, en écrivant par ex. 

Jean-Marc habite...

Les prédictions devraient inclure par ex. " à Nancy avec Julie".