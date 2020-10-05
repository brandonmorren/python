age = int(input("your age: "))

section = ""

if age <= 5:
    print("you are too young")
else:
    if 6 <= age <= 7:
        section = "beavers"
    elif 8 <= age <= 10:
        section = "cubs"
    elif 11 <= age <= 13:
        section = "scouts"
    elif 14 <= age <= 18:
        section = "explorers"
    else:
        section = "leaders"
    print("you'll be assigned to the " + section)
