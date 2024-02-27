def main():
    travel_log = [
        {
            "country": "France",
            "visits": 12, 
            "cities": ["Paris", "Lille", "Dijon"]
        },
        {
            "country": "Germany",
            "visits": 5,
            "cities": ["Berlin", "Hamburg", "Stuttgart"]
        },
    ]
    add_new_country(country="Russia", visits=2, cities=["Moscow", "Saint Petersburg"], travel_log=travel_log)
    print(travel_log)

def add_new_country(country, visits, cities, travel_log):
    new_country = {
        "country": country,
        "visits": visits,
        "cities": cities,
    }
    travel_log.append(new_country)

if __name__ == "__main__":
    main()