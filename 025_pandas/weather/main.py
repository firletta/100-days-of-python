from pandas import read_csv

WEATHER_DATA_FILE = "weather_data.csv"
WEATHER_DATA = read_csv(WEATHER_DATA_FILE)

def get_temp_list():
    temperatures = WEATHER_DATA["temp"].tolist()
    return temperatures

def average_temp():
    return WEATHER_DATA["temp"].mean()

def max_temp():
    return WEATHER_DATA["temp"].max()

def day_with_max_temp():
    return WEATHER_DATA["day"][WEATHER_DATA["temp"].idxmax()]

def weekday_temperature(weekday):
    return WEATHER_DATA["temp"][WEATHER_DATA["day"] == weekday]

def convert_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def main():
    print("(づ ￣ ³￣)づ")
    print(f"Average temperature: {average_temp()}°C")
    print(f"Max temperature: {max_temp()}°C")
    print(f"Day with max temperature: {day_with_max_temp()}")
    print(f"Temperature on Monday:{convert_to_fahrenheit(weekday_temperature("Monday")).values[0]}°F")

if __name__ == "__main__":
    main()

