import requests
from typing import Dict, Any

class Sheety:
    """A client for the Sheety API to interact with Google Sheets."""

    def __init__(self, api_token: str, endpoint: str):
        self.session = requests.Session()
        self.session.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json",
        }
        self.endpoint = endpoint

    def add_row(self, row: Dict[str, Any]) -> Dict[str, Any]:
        """Adds a row to the Google Sheet.

        Args:
            row: A dictionary containing data.

        Returns:
            A dictionary containing the response from the API.
        """
        try:
            response = self.session.post(self.endpoint, json={"workout": row}, headers=self.session.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            # Log or handle exception as appropriate
            raise RuntimeError(f"API request failed: {e}") from e