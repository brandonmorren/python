import xml.etree.ElementTree as ET
xmlDoc = ET.parse("./Files chapter 9/plants.xml")
root = xmlDoc.getroot()


def choice_input(choice_user):
    while choice_user not in ["A", "a", "H", "h", "L", "l"]:
        choice_user = input("your choice: ")
    return choice_user


def alphabet():
    list_plants_alphabet = []
    for plant in root.iter("plant"):
        price = plant[4].text
        name = plant[0].text
        list_plants_alphabet.append([name, price])
    list_plants_alphabet.sort()
    return list_plants_alphabet


def price_h_t_l():
    list_plants_alphabet = []
    for plant in root.iter("plant"):
        price = plant[4].text
        name = plant[0].text
        list_plants_alphabet.append([price, name])
    list_plants_alphabet.sort()
    list_plants_alphabet.reverse()
    return list_plants_alphabet


def price_l_t_h():
    list_plants_alphabet = []
    for plant in root.iter("plant"):
        price = plant[4].text
        name = plant[0].text
        list_plants_alphabet.append([price, name])
    list_plants_alphabet.sort()
    return list_plants_alphabet


print("list of plants, sorted by")
print("\t", "A: Alphabet")
print("\t", "H: Price (high to low)")
print("\t", "L: Price (low to high)")
choice = input("your choice: ")
choice_input_user = choice_input(choice)
print()

if choice_input_user in ["A", "a"]:
    list_plants = alphabet()
    for plants in list_plants:
        print(plants[1], "|", plants[0])
elif choice_input_user in ["H", "h"]:
    list_plants = price_h_t_l()
    for plants in list_plants:
        print(plants[0], "|", plants[1])
elif choice_input_user in ["L", "l"]:
    list_plants = price_l_t_h()
    for plants in list_plants:
        print(plants[0], "|", plants[1])



