import requests
from datetime import datetime
import pytz

LOCATION = {"latitude": 50.026403, "longitude": 14.542004}


class SpaceData:

    def __init__(self):
        self.session = requests.Session()
        self.iss_location = None

    def update_iss_location(self):
        response = self.session.get("http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = response.json()
        self.iss_location = (float(data["iss_position"]["latitude"]),
                             float(data["iss_position"]["longitude"]))

    def get_sunrise_sunset(self, latitude, longitude):
        response = self.session.get(
            f"https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}&formatted=0"
        )
        response.raise_for_status()
        data = response.json()["results"]
        sunrise = datetime.fromisoformat(
            data["sunrise"]).replace(tzinfo=pytz.utc)
        sunset = datetime.fromisoformat(
            data["sunset"]).replace(tzinfo=pytz.utc)
        return sunrise, sunset

    def is_daytime(self, latitude, longitude):
        sunrise, sunset = self.get_sunrise_sunset(latitude, longitude)
        return sunrise < datetime.now(pytz.utc) < sunset

    def is_iss_overhead(self, latitude, longitude):
        if not self.iss_location:
            self.update_iss_location()
        iss_lat, iss_lng = self.iss_location
        return latitude - 5 <= iss_lat <= latitude + 5 and longitude - 5 <= iss_lng <= longitude + 5


def main():
    space_data = SpaceData()
    print("Look up!" if space_data.
          is_iss_overhead(LOCATION["latitude"], LOCATION["longitude"])
          and space_data.is_daytime(LOCATION["latitude"], LOCATION["longitude"]
                                    ) else "Don't look up! :(")


if __name__ == "__main__":
    main()
