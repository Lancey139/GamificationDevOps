# Gamification_DevOps

Plateforme développée dans le but de s'interfacer avec une usine CI/CD : chaque animation est connectée à un job, lorsque celui-ci échoue les moteurs sont actionnés.
L'objectif est de gamifier la surveillance de l'usine de build DevOps pour remettre la qualité au centre de l'attention de l'équipe.
Dans ce code, l'interface entre la plateforme et le serveur se fait via un protocole USB mais une version existe également via le réseau.

Un aperçu de la plateforme est disponible au lien suivant : https://youtu.be/f3_C8oa5OVI

# Dépendances externes

Le module permettant la communication avec le serveur Jenkins

https://python-jenkins.readthedocs.io/en/latest/index.html
pip install python-jenkins
pip3 install --upgrade requests

Le module permettant de lire le fichier XML
https://lxml.de/installation.html
sudo apt-get build-dep python3-lxml
pip3 install lxml

Le module permettant la comunication serie
pip3 install pyserial

Autoriser l'utilisateur courant a acceder au port serie
adduser nom_utilisateur dialout
