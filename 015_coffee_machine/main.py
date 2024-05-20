from menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def main():
    global profit
    drinks = list(MENU.keys())
    while True:
        order = input(f"What would you like? ({'/'.join(drinks)}): ").lower()
        if order in drinks:
            order_details = MENU[order]
            order_ingredients = order_details["ingredients"]
            order_cost = order_details["cost"]
            if sufficient_resources(order_ingredients):
                added_coins = process_coins()
                while added_coins < order_cost:
                    print(f"{order.capitalize()} costs ${order_cost}.",
                          f"Current count: ${added_coins}. Please add coins.")
                    added_coins += process_coins()
                change = round(added_coins - order_cost, 2)
                if change > 0:
                    print(f"Here is ${change} in change.")
                for ingredient in order_ingredients:
                    resources[ingredient] -= order_ingredients[ingredient]
                profit += order_cost
                print(f"Enjoy your {order}.")
        elif order == "report":
            print(f"Water: {resources['water']}ml\n"
                  f"Milk: {resources['milk']}ml\n"
                  f"Coffee: {resources['coffee']}g\n"
                  f"Money: ${profit}")
        elif order == "off":
            break
        else:
            print("Invalid option. Please enter",
                  f"{', '.join(drinks[:-1])} or {drinks[-1]}.")


def sufficient_resources(order_ingredients):
    insufficient_ingredients = [
        ingredient for ingredient in order_ingredients 
        if order_ingredients[ingredient] >= resources[ingredient]
    ]
    if insufficient_ingredients:
        print(f"Sorry there is not enough ingredients",
              f"({', '.join(insufficient_ingredients)}).")
        return False
    else:
        return True


def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


if __name__ == "__main__":
    main()