number1 = input("Enter a number: ")
number2 = input("Enter another number: ")

try:
    number1 = float(number1)
    number2 = float(number2)

except ValueError:
    print("Type in numeric values. ")

print(number1+number2)
