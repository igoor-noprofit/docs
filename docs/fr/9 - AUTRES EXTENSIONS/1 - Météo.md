Cette extension rajoute des informations contextuelles sur la météo (température, vent etc.) au contexte, c.-à-d.. l'ensemble des informations qui sont envoyées à l'IA pour générer des prédictions (cf. [[1 - Quatre outils d’aide à la  communication]]).

<div style="background:red;color:#fff; padding: 10px">
ATTENTION: pour pouvoir fonctionner, le service nécessite de récuperer votre position actuelle tous les 10 minutes, basée sur l'adresse IP de votre connexion Internet. La précision de la position est variable. 
Cette extension n'est donc pas utilisable hors-ligne.
</div>


## Activation de l'extension

Allez dans

*Paramètres > Extensions > Contexte > Weather :*

![[../assets/weather_activate.png]]

et activez l'extension à travers le switch. 

**RAPPEL : Vous devez redémarrer IGOOR quand vous activez (ou désactivez) des extensions.**

## Configuration de l'extension

Allez dans : 

*Accueil > Gestion de la météo*

![[../assets/weather_activated.png]]

Cliquez l'icône des paramètres de l'extension.
L'extension fonctionne grâce à un service gratuit fourni par https://open-meteo.com/ (à partir de la version 0.3.5.0), et ne nécessite pas d'abonnement.

## Version précédentes

Les versions précédentes nécessitent de vous inscrire et récupérer votre clé API ici :

[Obtenir une clé API gratuite Openweathermap](https://home.openweathermap.org/users/sign_up){target: blank}


![[../assets/weather_config.png]]

## Adresse domicile

Vous pouvez insérer l'adresse exacte de votre domicile. **Cette adresse n'est jamais communiquée à l'extérieur ; elle est utilisée à l'intérieur d'IGOOR pour la comparer avec celle mise à jour automatiquement, afin de comprendre si l'utilisateur est à la maison.**

Sauvegardez vos modifications.
## Vérification

Une fois que vous activez la météo, vous verrez la température dans la barre de haut :

![[../assets/weather_icon_topbar.png]]

A partir de ce moment, les informations de la méteo sont ajoutées aux prédictions de phrases.
