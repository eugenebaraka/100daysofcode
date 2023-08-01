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

# TODO: 1. Ask user what they would like

def serve_drink(choice):

    profit = 0

    # to turn the machine off
    if choice.lower() == "off":
        pass
    # check resources if we have enough resources
    ingredients = MENU[choice]["ingredients"]
    for ingredient, amount in ingredients.items():
        if resources[ingredient] < amount:
            print(f"Sorry there is not enough {ingredient}☹️")
            # TODO: stop the program here
        remaining_resources = resources[ingredient] - amount
        resources.update({ingredient:remaining_resources})
    # Ask for coins
    cost = MENU[choice]["cost"]
    to_continue = int(input(f"Your {choice} will cost ${cost}. Press 1 to buy and 0 if you are broke for this: "))
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
                        print(f"You are too broke to buy this bro!😂 Find someone to lend you ${broke_by}!!")
        if total_so_far >= cost:
            change = "{:.2f}".format(total_so_far - cost)
            print(f"Here's your {change} in change.\nHere's your {choice}. Bonne appetit!")

            # calculate profit
            profit += cost

    if choice == "report":
        resources["Money"] = profit
        return resources

    else:
        pass


drink_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
if drink_choice in ["espresso", "latte", "cappuccino"]:
    serve_drink(choice=drink_choice)




# TODO: 2. Turn off machine by entering "off" to the prompt

# TODO: 3. Print "report"


