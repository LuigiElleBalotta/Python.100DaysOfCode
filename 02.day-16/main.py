# import another_module
# print(another_module.another_variable)
#
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
# from cartoon import paintPikachu
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander", "Bulbasaur"])
table.add_column("Type", ["Electric", "Water", "Fire", "Grass"])
table.align = "l"
print(table)

# paintPikachu()
print("=====================================")
print("Welcome to the Coffee Shop!")

coffeeMachine = CoffeeMaker()
moneyMachine = MoneyMachine()
menu = Menu()

while True:
    order = input("What would you like? (" + menu.get_items() + "): ")
    if order == "off":
        print("Turning off the coffee machine...")
        break
    elif order == "report":
        coffeeMachine.report()
        moneyMachine.report()
        continue
    elif order == "refill":
        coffeeMachine.refill()
        continue
    else:
        drink = menu.find_drink(order)
        if drink is not None:
            if coffeeMachine.is_resource_sufficient(drink):
                if moneyMachine.make_payment(drink.cost):
                    coffeeMachine.make_coffee(drink)
