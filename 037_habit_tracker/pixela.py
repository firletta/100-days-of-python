from typing import Dict, Optional
import requests

class PixelaClient:
    """Client for interacting with the Pixela API."""
    
    def __init__(self, endpoint: str, headers: Dict[str, str]):
        self.endpoint = endpoint
        self.headers = headers

    def create_graph(self, graph_id: str, name: str, unit: str, type: str, color: str, timezone: str, self_sufficient: str, is_secret: bool, publish_optional_data: bool) -> Optional[Dict]:
        """Creates a graph in Pixela."""
        url = f"{self.endpoint}/graphs"
        body = {
            "id": graph_id,
            "name": name,
            "unit": unit,
            "type": type,
            "color": color,
            "timezone": timezone,
            "selfSufficient": self_sufficient,
            "isSecret": is_secret,
            "publishOptionalData": publish_optional_data
        }
        response = requests.post(url=url, json=body, headers=self.headers)
        return self._handle_response(response)

    def post_pixel(self, graph_id: str, date: str, quantity: str) -> Optional[Dict]:
        """Posts a pixel to a specific graph."""
        url = f"{self.endpoint}/graphs/{graph_id}"
        body = {"date": date, "quantity": quantity}
        response = requests.post(url=url, json=body, headers=self.headers)
        return self._handle_response(response)

    def update_pixel(self, graph_id: str, date: str, quantity: str) -> Optional[Dict]:
        """Updates a pixel on a specific graph."""
        url = f"{self.endpoint}/graphs/{graph_id}/{date}"
        body = {"quantity": quantity}
        response = requests.put(url=url, json=body, headers=self.headers)
        return self._handle_response(response)

    def delete_pixel(self, graph_id: str, date: str) -> Optional[Dict]:
        """Deletes a pixel from a specific graph."""
        url = f"{self.endpoint}/graphs/{graph_id}/{date}"
        response = requests.delete(url=url, headers=self.headers)
        return self._handle_response(response)

    def _handle_response(self, response: requests.Response) -> Optional[Dict]:
        """Handles the API response, returning JSON data if successful, or None if not."""
        if response.ok:
            return response.json()
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None