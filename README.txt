Documentation de l'Application Super-Trefle

Qu'est-ce que Super-Trefle ?
Super-Trefle est une application web développée pour fournir des informations détaillées sur différentes plantes en utilisant l'API Trefle. 
L'application permet aux utilisateurs de rechercher des plantes par nom, de trouver des informations sur leur croissance et leur entretien, ainsi que de rechercher des plantes par caractéristiques spécifiques.

Fonctionnalités et Services :

1. Recherche de Plantes par Nom :
Cette fonctionnalité permet aux utilisateurs de rechercher des plantes en saisissant leur nom dans un champ de recherche.
Les résultats de la recherche affichent les plantes correspondant au nom spécifié, avec leur nom commun, leur nom scientifique ainsi que l'image de la plante en question.

2. Recherche d'Informations sur la Croissance et l'Entretien :
Cette fonctionnalité permet aux utilisateurs d'obtenir des informations détaillées sur la croissance et l'entretien de chaque plante.
Les informations comprennent des descriptions de la croissance de la plante, ses besoins en lumière, en eau, en sol, etc.

3. Recherche de Plantes par Caractéristiques :
Cette fonctionnalité permet aux utilisateurs de rechercher des plantes en fonction de certaines caractéristiques spécifiques, telles que la couleur des fleurs,le type de feuillage, etc.
Les résultats de la recherche affichent les plantes correspondant aux critères spécifiés.

Test de l'application:

Exécution des tests unitaires détaillés dans le fichier tests_unit/test_api_trefle.py

docker run plantinfo python -m unittest discover -s tests -p '*test_api_trefle.py'

Exécution en local de l'application: 

Démarage du conteneur de l'application puis accès à l'application dans le navigateur web en visitant l'adresse indiquée :

docker run -d -p 5000:5000 trefle-gang

http://localhost:5000
