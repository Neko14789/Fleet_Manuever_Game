name = ["Hübsch", "Wobrock", "Wallach", "Altarkawi"]
vorname = ["Gerrit", "Nico", "Ben", "Mohammed"]
trys = 1000

name_list = []
import random
for x in range(trys):
    name_full = f"{random.choice(vorname)} {random.choice(name)}"
    valid = True
    for y in name_list:
        if y == name_full:
            valid = False
    if valid:
        name_list.append(name_full)
        print(name_full)