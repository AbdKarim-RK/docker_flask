# Projet Flask Dockerisé

## Description

Ce projet est une petite application web Flask qui affiche des informations personnelles. Il est conçu pour être minimaliste et facilement déployable grâce à Docker.

## Fonctionnalités

* Affichage d'une page HTML simple avec des informations personnelles.
* Utilisation de Flask pour le serveur web.
* Dockerisé pour un déploiement facile et isolé.
* Compatible avec le rechargement automatique (debug mode) pour le développement.

## Structure du projet

```
flask_dir/project/
├── test.py             # Application Flask
├── requirements.txt    # Dépendances Python
├── Dockerfile          # Dockerfile pour containeriser l'application
├── docker-compose.yml  # Fichier docker-compose pour lancer le projet
```

## Prérequis

* Python 3.11
* Docker
* Docker Compose (optionnel, pour faciliter le lancement)

## Installation et utilisation

### 1. Localement avec Python

```bash
# Cloner le projet
git clone <URL_DU_REPO>
cd flask_dir/project

# Créer un environnement virtuel
python3 -m venv venv
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Lancer le serveur Flask
python test.py
```

Ouvrir ensuite votre navigateur sur : [http://127.0.0.1:5000](http://127.0.0.1:5000)

### 2. Avec Docker

```bash
# Construire l'image Docker
docker build -t project-web .

# Lancer le conteneur
docker run -p 5000:5000 project-web
```

### 3. Avec Docker Compose

```bash
docker compose up --build
```

Accéder ensuite à l'application via : [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Remarques

* L'application utilise `host="0.0.0.0"` pour que Flask soit accessible depuis l'extérieur du conteneur Docker.
* Le mode `debug=True` permet le rechargement automatique lors des modifications.
