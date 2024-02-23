import requests
import os
from urllib.parse import urlencode


class Api:
    def __init__(self):
        self.token = os.environ.get("API_TOKEN")
        self.url_base = "https://trefle.io/api/v1/plants/"

    def get_plants_by_name(self, plant_name):
        query = plant_name
        url = self.url_base + f"search?token={self.token}&q={query}"
        try:
            response = requests.get(url)
            response.raise_for_status() # Raise an exception for HTTP errors
            print(response.json())
            data = response.json()['data']
            print(data[0]["id"])
            return data

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None
