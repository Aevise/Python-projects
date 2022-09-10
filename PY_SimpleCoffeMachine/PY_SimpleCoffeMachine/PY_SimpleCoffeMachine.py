from PY_Coins import Coins
from PY_CoffeeRecipes import Recipes

machine_status = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0
}

def printReport(onlyPrint = True) -> list:
    """
    Prints the content of the coffee machine.
    """
    containers = list(machine_status.keys())
    report = []
    for item in containers:
        if(item == "water" or item == "milk"):
            print(f"{item}: {machine_status[item]}ml")
            report.append(f"{item}: {machine_status[item]}ml")
        elif(item == "coffee"):
            print(f"{item}: {machine_status[item]}g")
            report.append(f"{item}: {machine_status[item]}g")
        else:   
            print(f"{item}: {machine_status[item]}")
            report.append(f"{item}: \u0024 {machine_status[item]}") 

    if(onlyPrint == False):
        return report       

def checkMaterials(recipe: dict, product: str) ->bool:
    """
    Inform whether machine can deliver a product or not
    """
    material_list = list(recipe[product].keys())
    material_list.pop()
    for material in material_list:
        if(machine_status[material] < recipe[product][material]):
            print(f"Sorry, not enough {material}. Please pick something else")
            return False
    return True

def insertMoney()->float:
    typeofCoins = list(Coins.keys())
    amount = 0
    value = 0
    for coin in typeofCoins:
        print(f"How many {coin}'s would you like to insert?: ", end = "")
        try:
            amount = int(input())
            value += (Coins[coin]*amount)
        except ValueError:
            print("Sabotage detected!")
            return 0
    return value
    
def checkMoney(insertedCash: float, product: str)->bool:
    if(insertedCash >= Recipes[product]["Price"]):
        return True
    else:
        return False

def countChange(insertedCash: float, product: str)->float:
    return (insertedCash - Recipes[product]["Price"])

def useMaterials(product: str):
    product_list = list(Recipes[product].keys())
    product_list.pop()
    for item in product_list:
        machine_status[item] -= Recipes[product][item]

turnedOn = True
action = ""
enoughMaterials = True
products = list(Recipes.keys())
buyersMoney = 0

while turnedOn == True:
    action = input("What would you like? (espresso/latte/cappuccino): ").capitalize()
    if(action == "Report"):
        printReport()
    elif(action == "Off"):
        turnedOn = False
    elif(action in products):
        if(checkMaterials(Recipes, action) == True):
            buyersMoney = insertMoney()
            if(checkMoney(buyersMoney, action) == True):
                buyersMoney = countChange(buyersMoney, action)
                machine_status["Money"] += Recipes[action]["Price"]
                print("Here is yours $", buyersMoney, "in change!")
                useMaterials(action)
                print(f"Please enjoy your {action}")
            else:
                print(f"Sorry, you don't have enough money to buy {action}.")

        