my_list = [[1,0,1,0],[0,1,1,0],[0,1,1,1],[0,0,0,1]]

linje = ""

for liste in my_list:
    linje = ""
    for i in liste:
        linje += str(i) + " "
    print(linje)

print("")

del my_list[0]
del my_list[-1]
for liste in my_list:
    linje = ""
    for i in liste:
        linje += str(i) + " "
    print(linje)

