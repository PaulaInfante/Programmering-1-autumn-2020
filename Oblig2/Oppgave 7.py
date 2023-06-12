import random
print("Skriv inn antall spillere")
antallspillere = int(input())

spillere = [None] * antallspillere

for spiller in range(0,antallspillere):
    for pil in range(0,5):
        pilverdi = random.randrange(0,50)
        print("spiller", (spiller+1), "kastet en pil og fikk",pilverdi,"poeng")

        if spillere[spiller] == None:
            spillere[spiller] = 0
        spillere[spiller] += pilverdi

spillere.sort()
print("plassering")
for spiller in range(0,antallspillere):
    print("spiller", (spiller+1), "fikk totalt", spillere[spiller],"poeng")



