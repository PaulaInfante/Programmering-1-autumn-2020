firstName = input("Enter first name: ")
lastName = input("Enter last name: ")
age = input("Enter your age: ")

with open("guest.txt","a") as file:
    file.write(firstName + "," + lastName + "," + age + "\n")