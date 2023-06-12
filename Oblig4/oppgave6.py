import json

firstName = input("Enter first name: ")
lastName = input("Enter last name: ")
age = input("Enter your age: ")

fileContent = []

try:
    with open("guests,json","r") as file:
        fileContent = json.load(file)
except:
    fileContent = []

fileContent.append({"name":firstName, "lastname":lastName,"age":age})

with open("guests.json", "w") as file:
    json.dump(fileContent, file)
