from data import resources
from data import MENU

loop = True
water = resources['water']
milk = resources['milk']
coffee = resources['coffee']
while loop:
    userinput = input("What would you like? (espresso/latte/cappuccino): ")
    money = 0

    water_ingredient = MENU[userinput]["ingredients"]["water"]
    milk_ingredient = MENU[userinput]["ingredients"]["milk"]
    coffee_ingredient = MENU[userinput]["ingredients"]["coffee"]


    def resources():
        return f"\n Water: {water} \n Milk: {milk} \n Coffee: {coffee} \n Money: ${money} "


    print("Please insert coins.")

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_amount = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)

    return_amount = round(total_amount - MENU[userinput]["cost"], 2)


    def money_count():
        if return_amount >= 0:
            return True
        else:
            return False


    def resource_availabe():
        global water, water_ingredient, milk_ingredient, milk, coffee_ingredient, coffee
        if water >= water_ingredient and milk >= milk_ingredient and coffee >= coffee_ingredient:
            return True
        else:
            return False


    if userinput == "report":
        print(resources())
    elif userinput == "off":
        loop = False
    elif userinput == "espresso" or userinput == "latte" or userinput == "cappuccino" and money_count() and resource_availabe():
        water -= water_ingredient
        milk -= milk_ingredient
        coffee -= coffee_ingredient
        money += MENU[userinput]["cost"]
        print(f"Here is ${return_amount} in change")
        print(f"Here is your {userinput} ☕. Enjoy!")
    elif not money_count():
        print("Sorry that's not enough money. Money refunded")
    else:
        print("Sorry Ingredients not available at this item")