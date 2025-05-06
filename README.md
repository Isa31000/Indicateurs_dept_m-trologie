Description projet  

Cellule 1 : Récupération de la data nettoyée  

Cellule 2: Définition de la palette couleurs   

Cellule 3: Fonctions de mise en forme (titres, zones de commentaires, tableau et graphiques)  

Cellule 4 : fonction de traitement de données :  

1/ tracée du grid (avec création des variables globales fig (où seront dessinés mes axes), texte2c, texte3, texte4 et texte5 (où on mettra ensuite les commentaires interactifs pour l'utilisateur)  

2/traitement des données avec la variable date de référence (qu’on récupére plus tard) 

Cellule 5: Champ de saisie de la date avec widgets 

1/initialisation des widgets (emplacement date/ bouton de validation) 

2/fonction de validation du bouton avec :  

Clear output 

Verification format de la date  

Appel de la fonction de traitement de données (de la cellule 4)  

3/Connexion du bouton à la fonction de validation du bouton  

4/Affichage  


Cellule 6:  

1/ initialisation des widgets (avec mes 4 zones de commentaires + 1 bouton + output)  

2/fonction de genération graphique  

Clear output 

Recup commentaires saisis par l’utilisateur  

Fig.Canvas.draw  

3/fonction de validation du bouton :    

Clear output  

Recup commentaires  

Appel fonction generer graphique   

4/connexion du bouton à la fonction de validation bouton  

5/Affichage  
