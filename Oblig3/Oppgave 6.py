Menu = [
    {
        "name":"Yoghurt",
        "price":25
    },
    {
        "name":"Litago",
        "price":25

    },
    {
        "name":"Sandwich",
        "price":40
    },
    {
        "name":"Cola",
        "price":30
    },
    {
        "name":"Fruit",
        "price":15
    }
]

running = True
shoppingCart = []

def printMenu():
    print("Here is the menu")
    for item in Menu:
        print(item["name"], ": ", item["price"])

    print("")

def printShoppingCart():
    print("Shopping cart")

    for item in shoppingCart:
        print(item["name"], ":", item["amount"], "stk")

def addItem():
    userInput = input("Enter name:")
    userInputAmount = int(input("Enter amount:"))
    for item in Menu:
        if item["name"] == userInput:
            for shoppingCartItem in shoppingCart:
                if shoppingCartItem["name"] == userInput:
                    shoppingCart["amount"] += userInputAmount
                    return
            shoppingCart.append({"name":userInput, "amount":userInputAmount})
            return

    print("Could not find an item named", userInput,".Pleace retry.")
    addItem()

def removeItem():
    userInput = input("Enter name:") 

    for item in shoppingCart: 
        if item["name"] == userInput:
            shoppingCart.remove(item)
            return  
            print("Could not find a item named", userInput,". Please retry.")

def getPrice():
    price = 0
    for shoppingCartItem in shoppingCart:
        for item in Menu:
            if shoppingCart["name"] == item["name"]:
                price += shoppingCart["amount"] * item["price"]
                 
    print("Total price:", price, "kr")
    return price

def checkout():
    price = getPrice()
    print("Buy items:")
    printShoppingCart()
    global running
    running = False


while running:
    print("==========Welcome to the SiØ Kafeteria==========")
    print("")
    printMenu()

    print("Your options are: ")
    print("quit - exit the program")
    print("show - shows the shopping cart")
    print("ready - ready to check out and pay")
    print("add - add item(s) to shopping cart. Make sure to write an item that is actually in the menu")
    print("remove - Remove an item from the shopping cart")

    print("")

    userInput = input("Option:")

    if userInput == "show":
        printShoppingCart()

    if userInput == "ready":
        checkout()

    if userInput == "add":
        addItem()

    if userInput == "remove":
        removeItem()

    if userInput == "quit":
        running = False


