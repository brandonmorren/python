import xml.etree.ElementTree as ET
set_game_txtFile = set()
set_game_XMLFile = set()
set_intersection = set()
set_difference_txtFile = set()
set_difference_XMLFile = set()

with open("./Files Chapter 10/games.txt") as file:
    line = file.readline().rstrip()
    record = line.split(",")
    while line:
        type = record[7]
        if not type.isdigit():
            set_game_txtFile.add(record[7].strip("'"))
        line = file.readline().rstrip()
        record = line.split(",")

xmlDoc = ET.parse("./Files Chapter 10/games.xml")
root = xmlDoc.getroot()
for customer in root.iter("type"):
    set_game_XMLFile.add(customer.text)

print("in the txt-file:", len(set_game_txtFile), "types of games")
print("in the xml-file:", len(set_game_XMLFile), "types of games")
set_intersection = set_game_txtFile.intersection(set_game_XMLFile)
print("the types that occur in both files: ")
print(set_intersection)
set_difference_txtFile = set_game_txtFile.difference(set_game_XMLFile)
print("the types that only occur in txt file: ")
print(set_difference_txtFile)
set_difference_XMLFile = set_game_XMLFile.difference(set_game_txtFile)
print("the types that only occur in xml file: ")
print(set_difference_XMLFile)
