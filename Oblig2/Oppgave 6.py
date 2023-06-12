rente = 0.06
nedbetaling = 7
laan = 600000
totalnedbetaling = 0

for i in range(0,nedbetaling):
    totalnedbetaling = ((laan - totalnedbetaling) * rente) + (laan/nedbetaling)
    print(totalnedbetaling)

