import requests
import os
from urllib.parse import urlencode


class Api:
    def __init__(self):
        self.token = os.environ.get("API_TOKEN")
        self.url_base = "https://trefle.io/api/v1/"

    def get_plants_by_name(self, plant_name):
        query = plant_name
        url = self.url_base + "plants/" + f"search?token={self.token}&q={query}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()['data']
            return data

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

    def get_plants_by_fields(self, filters=None, current_section=None):
        # Commence par l'URL de base et ajoute le token d'API
        url = f"{self.url_base}species?"

        # Ajoute les filtres à l'URL, si présents
        if filters:
            for key, value in filters.items():
                # Encodage manuel des clés et valeurs de filtre pour les ajouter à l'URL
                url += f"&filter%5B{current_section}_{key}%5D={value}&token={self.token}"

        print(url)

        # Effectue la requête GET
        response = requests.get(url)

        # Gère la réponse de la requête
        if response.status_code == 200:
            # Si la requête réussit, renvoie les données JSON
            return response.json()
        else:
            # Gère les éventuelles erreurs de la requête
            return {'error': f'Requête échouée avec le statut {response.status_code}'}