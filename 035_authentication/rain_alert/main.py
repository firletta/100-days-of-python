import requests
from settings import WEATHER_AUTH_KEY, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER
from twilio.rest import Client

LAT = 50.0368
LON = 14.5250
PHONE_NUMBER = "+420775652081"


def main():
    if umbrella_needed(lat=LAT, lon=-LON):
        message = "It's going to rain today. Remember to bring an umbrella!"
        send_sms(phone_number=PHONE_NUMBER, text=message)


def fetch_48h_forecast(lat: float, lon: float) -> dict:
    """
    Fetches the 48-hour weather forecast for a specific location.

    Args:
        lat (float): The latitude of the location.
        lon (float): The longitude of the location.

    Returns:
        dict: The 48-hour weather forecast data in JSON format.
    """
    params = {
        "lat": lat,
        "lon": lon,
        "appid": WEATHER_AUTH_KEY,
        "units": "metric",
        "exclude": "current,minutely,daily"
    }
    response = requests.get("https://api.openweathermap.org/data/3.0/onecall",
                            params=params)
    return response.json()


def umbrella_needed(lat: float, lon: float) -> bool:
    """
    Check if an umbrella is needed based on the weather forecast for the next
    12 hours.

    Args:
        lat (float): The latitude of the location.
        lon (float): The longitude of the location.

    Returns:
        bool: True if an umbrella is needed within the next 12 hours, False otherwise.
    """
    hourly_forecast = fetch_48h_forecast(lat=lat, lon=lon)["hourly"]
    return any(
        int(hour["weather"][0]["id"]) < 700 for hour in hourly_forecast[:12])


def send_sms(phone_number, text):
    """
    Sends an SMS message to a specified phone number using Twilio's messaging service.

    Args:
        phone_number (str): The destination phone number for the SMS message.
        text (str): The content of the SMS message to be sent.

    Returns:
    None. However, it prints the message text to the console.
    """
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        from_=TWILIO_PHONE_NUMBER,
        body=text,
        to=phone_number
        )
    print(text)


if __name__ == "__main__":
    main()
