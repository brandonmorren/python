set_1ITF = set()
set_2ITF = set()
list_name = []

with open("./Files Chapter 10/first_names1ITF.txt") as file:
    name = file.readline().rstrip()
    while name:
        set_1ITF.add(name)
        name = file.readline().rstrip()

with open("./Files Chapter 10/first_names2ITF.txt") as file:
    name = file.readline().rstrip()
    while name:
        set_2ITF.add(name)
        name = file.readline().rstrip()

print("in 1ITF there are", len(set_1ITF), "different first names")
print("in 2ITF there are", len(set_2ITF), "different first names")
set_intersection = set_1ITF.intersection(set_2ITF)
print("these are the", len(set_intersection), "first names appearing in 1ITF and 2ITF")
for name in set_intersection:
    list_name.append(name)
list_name.sort()
for item in list_name:
    print(item)