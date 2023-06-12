#samarbeid med Ida Tveiterås

groceries = {}
running = True

def addItem(name,amount):
    groceries[name] = amount

def removeItem(name):
    groceries[name] = 0

def showItems():
    print(groceries)

while running:
    print("Welcome to best-shopping-list!")
    print("")
    print("s: show list")
    print("a: add to list")
    print("d: delete from list")
    print("e: exit")

    userInput = input("Choose between s/a/d/e:")

    if userInput == "s":
        showItems()

    if userInput == "a":
        name = input("Grocery name:")
        amount = input("Amount:")
        addItem(name,amount)

    if userInput == "d":
        name = input("Grocery to delete:")
        removeItem(name)

    if userInput == "e":
        running = False 

