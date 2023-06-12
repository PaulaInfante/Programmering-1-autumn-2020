number1 = input("First number:\n")
operator = input("Operator(+,-,*,/,%,**,//):\n")
number2 = input("Second number:\n")


number1 = float(number1)
number2 = float(number2)

out = None

if operator == "+":
    out = number1 + number2
if operator == "-":
    out = number1 - number2
if operator == "*":
    out = number1 * number2
if operator == "/":
    out = number1 / number2
if operator == "%":
    out = number1 % number2
if operator == "**":
    out = number1 ** number2
if operator == "//":
    out = number1 // number2
print("Answer:" + str(out))
#brukte koden fra denne siden: https://levelup.gitconnected.com/3-ways-to-write-a-calculator-in-python-61642f2e4a9a
#jeg kunne ha gjort det på en enklere måte. den var den eneste jeg forstod