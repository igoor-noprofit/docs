**À partir de la version 1, IGOOR supporte plusieurs fournisseurs cloud d'IA**, ainsi que la possibilité d'utiliser votre IA locale.

## Comparatif des fournisseurs cloud d'IA

Voici un comparatif des fournisseurs cloud pour vous aider à choisir :

| CARACTERISTIQUES / FOURNISSEUR                                             | GROQ<br>                                                   | MISTRAL                                                              | CEREBRAS                                                                                    |
| -------------------------------------------------------------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| vitesse                                                                    | très bonne                                                 | très bonne sur leur petit modèle                                     | excellente, notamment sur les prompts plus longs                                            |
| prix                                                                       | gratuit dans les limites d'usage ou prix à la consommation | gratuit dans les limites d'usage ou prix à la consommation           | gratuit dans les 5$ de consommation offerts, automatiquement payant à la consommation après |
| rapport vitesse / prix                                                     | meilleur                                                   | dépendant du modèle                                                  | deuxième meilleur                                                                           |
| possibilité d'utiliser le fournisseur sans insérer vos données de paiement | ✅                                                          | ✅                                                                    | ❌                                                                                           |
| offre un modèle de reconnaissance vocale                                   | ✅                                                          | ✅                                                                    | ❌                                                                                           |
| modèles *open-source*                                                      | ✅                                                          | ❌                                                                    | ✅                                                                                           |
| vos données ne sont PAS utilisées pour entrainer le modèle                 | ✅                                                          | *opt-out* dans l'offre gratuite : vous devez spécifier votre souhait | ✅                                                                                           |
| serveurs en Europe                                                         | ✅                                                          | ✅                                                                    | à la fin de 2026                                                                            |
| respect de la vie privée                                                   | très bon                                                   | *opt-out* optionnel                                                  | bon                                                                                         |

Pour Groq, nous vous renvoyons à la [[2 - Configuration rapide]].

### Utiliser IGOOR gratuitement avec Mistral

Comme Groq, Mistral propose également ses modèles de prédictions textuels, ainsi qu'un très bon modèle de reconnaissance vocale. 
Il y a deux différences principales par rapport à Groq :

1) ses modèles ne sont pas open-source ni open-weights : cependant, toute leur infrastructure est en France et donc doit répondre au RGPD français, qui est très stricte. Vérifiez leur [politique de confidentialité](https://legal.mistral.ai/terms/privacy-policy?language=fr-FR 
2) leurs modèles plus larges ne sont pas aussi rapides que les modèles larges de Groq

Le processus pour obtenir une clé Mistral est semblable à celui de Groq. 
Allez sur :

[Obtenir une clé API gratuite Mistral](https://console.mistral.ai/)
![[../assets/console_mistral.png]]
Inscrivez-vous, et cliquez ensuite sur *Clés API* depuis le menu à gauche :

![[../assets/mistral_api_key.png]]

Cliquez ensuite sur *Ajouter une nouvelle clé* :

![[../assets/generate_api_key_mistral.png]]

Donnez un nom à la clé et cliquez sur *Nouvelle clé*. 

![[../assets/create_key_mistral.png]]

Vous pouvez créer autant de clé API que vous souhaitez, mais vous ne pouvez pas les afficher une deuxième fois. Cliquez sur *Copier* :

![[../assets/copy_mistral_key.png]]

Revenez dans le logiciel IGOOR, rentrez dans les paramètres (bouton en haut à droite) et cliquez sur l'onglet IA. 

![Coller la clé](../assets/paste_api_key.png)

Sélectionnez Mistral comme fournisseur, et collez ensuite la clé dans le champ Clé API. Cliquez ensuite le bouton *Enregistrer les paramètres principaux*.

Si vous souhaitez utiliser Mistral également pour la reconnaissance vocale dans le cloud, vous devez le spécifier manuellement. Voir [[2 - Reconnaissance vocale dans le cloud]]


### Tester IGOOR gratuitement avec Cerebras

À noter que : 

- **À partir du 17 juillet 2026, pour tester gratuitement Cerebras dans la limite de 5$ de crédit, vous devez renseigner vos données de paiement**. Au-delà de 5$ de consommation, vous allez automatiquement payer à la consommation.
- Également, **Cerebras ne propose pas de modèle de reconnaissance vocale dans le cloud**. De ce fait, si vous optez pour une reconnaissance vocale dans le cloud, vous allez devoir utiliser Groq ou Mistral.9

**Nous conseillons donc Cerebras exclusivement aux utilisateurs plus avancés.**