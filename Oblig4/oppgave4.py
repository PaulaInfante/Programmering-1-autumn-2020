try:
    with open("pi_digits.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")