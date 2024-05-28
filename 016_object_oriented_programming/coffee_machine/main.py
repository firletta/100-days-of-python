from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    coffee_maker = CoffeeMaker()
    menu = Menu()
    money_machine = MoneyMachine()

    while True:
        options = menu.get_items()
        order = input(f"What would you like? ({options}): ")
        if order == "off":
            break
        elif order == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            if menu.find_drink(order):
                drink = menu.find_drink(order)
                if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
            else:
                print("Invalid order. Please try again.")

if __name__ == "__main__":
    main()