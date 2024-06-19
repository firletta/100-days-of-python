from pandas import read_csv
from art import squirrel_ascii_art

SQUIRREL_FILE = "central_park_squirrel_data.csv"
SQUIRREL_DATA = read_csv(SQUIRREL_FILE, usecols=["Primary Fur Color"])

def get_colors_count():
    return SQUIRREL_DATA["Primary Fur Color"].value_counts()

def main():
    print(squirrel_ascii_art)
    color_counts = get_colors_count()
    print(color_counts)
    color_counts.to_csv("squirrel_colors.csv")

if __name__ == "__main__":
    main()