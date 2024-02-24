import unittest
from unittest.mock import patch, MagicMock
from api.apiTrefle import Api

import requests


class TestGetPlantsByName(unittest.TestCase):
    @patch('api.apiTrefle.requests.get')  # Assurez-vous que le chemin est correct
    def test_get_plants_by_name_success(self, mock_get):
        # Configurez le mock pour simuler une réponse réussie de l'API
        mock_get.return_value.json.return_value = {"data": [{"id": 236068, "common_name": "Coconut"}]}
        mock_get.return_value.status_code = 200
        api = Api()
        result = api.get_plants_by_name('coconut')
        id = result[0]["id"]
        self.assertEqual(id, 236068)

    @patch('api.apiTrefle.requests.get')
    def test_get_plants_by_name_http_error(self, mock_get):
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError()
        mock_get.return_value = mock_response
        api = Api()
        result = api.get_plants_by_name('coconut')
        self.assertIsNone(result)

    @patch('api.apiTrefle.requests.get')
    def test_get_plants_by_name_request_exception(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException()
        api = Api()
        result = api.get_plants_by_name('coconut')
        self.assertIsNone(result)


class TestGetPlantsByFields(unittest.TestCase):
    @patch('api.apiTrefle.requests.get')
    def test_get_plants_by_fields_success(self, mock_get):
        mock_get.return_value.json.return_value = {"data": [{"id": 266630, "common_name": "Arctic bramble"}]}
        mock_get.return_value.status_code = 200
        api = Api()
        filters = {"color": "red"}
        current_section = "flower"
        result = api.get_plants_by_fields(filters=filters, current_section=current_section)
        self.assertEqual(result["data"][0]["id"], 266630)
        self.assertEqual(result["data"][0]["common_name"], "Arctic bramble")

    @patch('api.apiTrefle.requests.get')
    def test_get_plants_by_fields_failure(self, mock_get):
        mock_get.return_value.status_code = 404
        api = Api()
        result = api.get_plants_by_fields()
        self.assertIn('error', result)
        self.assertEqual(result['error'], 'Requête échouée avec le statut 404')

    @patch('api.apiTrefle.requests.get')
    def test_get_plants_by_fields_with_filters(self, mock_get):
        api = Api()
        filters = {"color": "red"}
        current_section = "flower"
        api.get_plants_by_fields(filters=filters, current_section=current_section)
        called_url = mock_get.call_args[0][0]
        self.assertIn('filter%5Bflower_color%5D=red', called_url)

if __name__ == '__main__':
    unittest.main()
