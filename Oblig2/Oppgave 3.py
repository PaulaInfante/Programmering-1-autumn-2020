my_list = ["H","I","O","F"]
my_string = "H:I:O:F"
my_string2 = "HIOF"

hiofstreng= ""

for string in my_list:
    hiofstreng += string

print(hiofstreng)

print("")

my_string_liste = my_string.split(":")

print(my_string_liste)

print("")

my_string2_liste = list(my_string2)

print(my_string2_liste)
