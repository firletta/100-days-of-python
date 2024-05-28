from prettytable import PrettyTable


def main():
    table = PrettyTable()
    table.align = "l"
    pokemon_data = {
        "Pokemon Name": ["Pikachu", "Squirtle", "Charmander"],
        "Type": ["Electric", "Water", "Fire"]
    }
    for column_name, column_data in pokemon_data.items():
        table.add_column(column_name, column_data)
    print(table)

if __name__ == "__main__":
    main()

