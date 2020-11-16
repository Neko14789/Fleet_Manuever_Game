name = ["U", "V", "W", "X"]
vorname = ["A", "B", "C", "D"]

# name = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# vorname = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
trys = 1000     # Max Amount of Names

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
        debug = str(x)+ " "
        print( debug + name_full)
