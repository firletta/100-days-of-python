def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9/5 + 32

def main():
    weather_c = {
        "Monday": 12,
        "Tuesday": 14,
        "Wednesday": 15,
        "Thursday": 14,
        "Friday": 21,
        "Saturday": 22,
        "Sunday": 24,
    }

    # Convert weather from Celsius to Fahrenheit
    weather_f = {day: convert_to_fahrenheit(temp) for day, temp in weather_c.items()}
    print(weather_f)

if __name__ == "__main__":
    main()