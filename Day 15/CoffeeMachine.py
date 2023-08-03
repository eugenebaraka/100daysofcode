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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 1. Ask user what they would like
def is_sufficient(choice_ingredients):
    """Returns True when there is enough ingredients for the order and False otherwise."""
    for ingredient, amount in choice_ingredients.items():
        if amount > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True

def process_coins(cost:float):
    """Return the total calculated from the coins calculated."""

    to_continue = int(input(f"The drink will cost ${cost}. Press 1 to buy and 0 if you are broke for this: "))
    if to_continue == 1:
        quarters = int(input("Please insert coins.\nHow many quarters do you have?: "))
        total_so_far = quarters * 0.25
        # check if quarters are enough so far
        if quarters*0.25 < cost:
            dimes = int(input("How many dimes do you have?: "))
            # check if money is enough so far
            total_so_far += dimes*0.1
            if total_so_far < cost:
                nickels = int(input("How many nickels do you have?: "))
                total_so_far += nickels*0.05
                if total_so_far < cost:
                    pennies = int(input("How many pennies do you have?: "))
                    total_so_far += pennies*0.01
                    if total_so_far < cost:
                        broke_by = "{:.2f}".format(cost - total_so_far)
                        print(f"You are too broke to buy this bro!😂 Find someone to lend you ${broke_by}!! Money refunded.")
                        return False
        if total_so_far >= cost:
            change = round(total_so_far - cost, 2)
            # change = ":.2f".format()
            print(f"Here's your {change} in change!")
            return True

def make_coffee(choice:str, ingredients:dict):
    """Deduct the required ingredients from the resources."""
    for ingredient, amount in ingredients.items():
        resources[ingredient] -= amount
    print(f"Here's your {choice}. Bonne appetit!")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_sufficient(drink['ingredients']):
            cost = drink['cost']
            profit += cost
            if process_coins(cost):
                make_coffee(choice, drink['ingredients'])


