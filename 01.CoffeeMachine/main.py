MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def get_coins():
    print("Insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total


def make_espresso():
    total = get_coins()
    if total < MENU["espresso"]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    elif total > MENU["espresso"]["cost"]:
        # Check resources
        if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            print("Money refunded.")
        elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            print("Money refunded.")
        else:
            # Make coffee
            resources["water"] -= MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
            change = round(total - MENU["espresso"]["cost"], 2)
            print(f"Here is ${change} in change.")
            print("Here is your espresso. Enjoy!")
    free_machine_screen()


def make_latte():
    total = get_coins()
    if total < MENU["latte"]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    elif total > MENU["latte"]["cost"]:
        # Check resources
        if resources["water"] < MENU["latte"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            print("Money refunded.")
        elif resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            print("Money refunded.")
        elif resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            print("Money refunded.")
        else:
            # Make latte
            resources["water"] -= MENU["latte"]["ingredients"]["water"]
            resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
            resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
            change = round(total - MENU["latte"]["cost"], 2)
            print(f"Here is ${change} in change.")
            print("Here is your latte. Enjoy!")
    free_machine_screen()


def make_cappuccino():
    total = get_coins()
    if total < MENU["cappuccino"]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    elif total > MENU["cappuccino"]["cost"]:
        # Check resources
        if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            print("Money refunded.")
        elif resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            print("Money refunded.")
        elif resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            print("Money refunded.")
        else:
            # Make cappuccino
            resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
            resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
            resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
            change = round(total - MENU["cappuccino"]["cost"], 2)
            print(f"Here is ${change} in change.")
            print("Here is your cappuccino. Enjoy!")
    free_machine_screen()


def free_machine_screen():
    print("Welcome to the coffee machine!")
    print("What would you like? (espresso/latte/cappuccino):")
    # Get the prompt
    choice = input()
    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: $0.0")
    elif choice == "off":
        print("Machine is now off.")
        # Exit the program
        exit()
    elif choice == "refill":
        print("Refilling resources...")
        resources["water"] = 300
        resources["milk"] = 200
        resources["coffee"] = 100
        print("Resources refilled.")
        free_machine_screen()
    elif choice == "espresso":
        make_espresso()
    elif choice == "latte":
        make_latte()
    elif choice == "cappuccino":
        make_cappuccino()
    else:
        print("Invalid choice. Please try again.")
        free_machine_screen()


free_machine_screen()
