# LinkedIn Adder Bot

LinkedIn Adder est un script Python automatisé qui utilise Selenium pour ajouter automatiquement des personnes dans un domaine spécifique à votre réseau LinkedIn. Vous pouvez spécifier le domaine de recherche, le nombre de personnes à ajouter, et vos identifiants LinkedIn.

## Fonctionnalités

- Recherche de personnes dans un domaine spécifique sur LinkedIn
- Ajout automatique de connexions
- Prise en charge des identifiants LinkedIn sécurisés (avec `getpass` pour le mot de passe)
- Spécification du nombre d'ajouts à effectuer (jusqu'à 100)

## Prérequis

Avant de pouvoir exécuter ce script, assurez-vous d'avoir installé les éléments suivants :

- Python 3.x
- Selenium (`pip install selenium`)
- Google Chrome installé sur votre machine
- [ChromeDriver](https://chromedriver.chromium.org/downloads) correspondant à la version de votre navigateur Chrome

## Installation

1. Clonez ce dépôt ou téléchargez les fichiers directement.

```bash
git clone https://github.com/votre-utilisateur/linkedin-adder-bot.git
```
Installez les dépendances requises.
```bash
pip install selenium
```
Téléchargez ChromeDriver et ajoutez-le à votre PATH, ou spécifiez son chemin dans le script Python si nécessaire.


##Utilisation
Ouvrez un terminal dans le répertoire du script.

Exécutez le script Python.

```bash
python linkedin_adder_bot.py
```

Entrez les informations requises lorsque le script vous le demande :

Domaine de recherche : Le domaine ou secteur d'activité des personnes que vous souhaitez ajouter (par exemple : "RH Cybersécurité").
E-mail LinkedIn : Votre identifiant de connexion LinkedIn.
Mot de passe : Votre mot de passe LinkedIn (ceci est sécurisé avec getpass).
Nombre de personnes à ajouter : Le nombre de personnes que vous souhaitez ajouter à votre réseau (entre 1 et 100).
Le bot ouvrira une instance de Google Chrome, se connectera à votre compte LinkedIn, et commencera à ajouter des personnes dans le domaine spécifié.
