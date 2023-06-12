#task 2a)
a = d = 1
b = c = 2
if a == c and b == d or b == c:
    print("True")
else:
    print("False")

if a == c and (b == d or a == d):
    print("True")
else:
    print("False")

#task 2b)

if a == b and b == c or a == d:
    print("True")
