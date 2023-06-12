dyr = ["Hund","Katt","Reinsdyr","Elefant","Fisk"]

print(dyr[0])
print(dyr[4])

print("")

#Hvis man ikke vet lengden i listen, og man skal ha det siste elemetet i listen så kan man gjøre sånn her.

print(dyr[-1])

print("")

dyr.sort()
dyr.reverse()

print("Sortert alfaberisk reversert")
for etdyr in dyr:
  print(etdyr)