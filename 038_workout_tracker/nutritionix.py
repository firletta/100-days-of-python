import requests
from typing import Dict, Any

class Nutritionix:
    """A client for the Nutritionix API to fetch exercise data."""
    
    def __init__(self, api_id: str, api_key: str):
        self.session = requests.Session()
        self.session.headers.update({
            "x-app-id": api_id,
            "x-app-key": api_key,
            "Content-Type": "application/json",
        })
        self.endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
    
    def get_exercise_data(self, query: str) -> Dict[str, Any]:
        """Fetches exercise data based on a natural language query.
        
        Args:
            query: A string containing the natural language exercise query.
        
        Returns:
            A dictionary containing the exercise data.
        """
        try:
            response = self.session.post(self.endpoint, json={"query": query})
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            # Log or handle exception as appropriate
            raise RuntimeError(f"API request failed: {e}") from e