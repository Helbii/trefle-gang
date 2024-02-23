import requests

def search_plants_by_name(api_token, plant_name):
    url = f"https://trefle.io/api/v1/plants/search?token={api_token}&q={plant_name}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        data = response.json()
        plants = data.get('data', [])
        return plants
        
    except requests.exceptions.RequestException as e:
        # Handle HTTP errors
        print(f"Error fetching data: {e}")
        return None
