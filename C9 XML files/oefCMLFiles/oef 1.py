import xml.etree.ElementTree as ET
xmlDoc = ET.parse("./Files chapter 9/plants.xml")
root = xmlDoc.getroot()

count = 1
for plant in root.iter("plant"):
    if plant[3].text == "SUN":
        print("plant", count, ":", plant[0].text, "(" + plant[1].text + ")")
        count += 1