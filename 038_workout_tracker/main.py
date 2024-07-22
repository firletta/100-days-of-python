import datetime as dt
from typing import List, Dict, Any
from nutritionix import Nutritionix
from sheety import Sheety
from config import NUTRITIONIX_API_ID, NUTRITIONIX_API_KEY, SHEETY_API_ENDPOINT, SHEETY_API_TOKEN

class WorkoutTracker:
    def __init__(self):
        self.nutritionix = Nutritionix(NUTRITIONIX_API_ID, NUTRITIONIX_API_KEY)
        self.sheety = Sheety(api_token=SHEETY_API_TOKEN, endpoint=SHEETY_API_ENDPOINT)

    def get_exercise_data_from_user_input(self) -> List[Dict[str, Any]]:
        """Fetches and returns exercise data based on user input."""
        query = input("Tell me about your exercise: ")
        try:
            exercise_data = self.nutritionix.get_exercise_data(query)
            return exercise_data.get("exercises", [])
        except Exception as e:
            print(f"Error fetching exercise data: {e}")
            return []

    def add_exercise_to_google_sheet(self, exercise: str, duration_min: float, calories: float) -> None:
        """Adds a single exercise entry to the Google Sheet."""
        now = dt.datetime.now()
        workout = {
            "date": now.strftime("%d/%m/%Y"),
            "time": now.strftime("%H:%M:%S"),
            "exercise": exercise,
            "duration": duration_min,
            "calories": calories,
        }
        try:
            self.sheety.add_row(workout)
        except Exception as e:
            print(f"Error adding data to Google Sheet: {e}")

    def run(self) -> None:
        """Main method to run the workout tracker."""
        exercise_data = self.get_exercise_data_from_user_input()
        for exercise in exercise_data:
            self.add_exercise_to_google_sheet(exercise=exercise["name"], duration_min=exercise["duration_min"], calories=exercise["nf_calories"])

if __name__ == "__main__":
    tracker = WorkoutTracker()
    tracker.run()