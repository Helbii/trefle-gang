# Utiliser une image de base Python officielle.
FROM python:3.8-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de dépendances et installer les dépendances
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copier le reste des fichiers de l'application dans le conteneur
COPY . .

# Définir la variable d'environnement pour exécuter l'application
# Ceci est utilisé par Flask pour identifier le fichier d'entrée
ENV FLASK_APP=app.py

# Exposer le port sur lequel l'application va s'exécuter
EXPOSE 5000

# Commande pour démarrer l'application
CMD ["flask", "run", "--host=0.0.0.0"]