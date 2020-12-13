import xml.etree.ElementTree as ET
xmlDoc = ET.parse("./Files chapter 9/drugs.xml")
root = xmlDoc.getroot()

for leaflet in root:
    leaflet.remove(leaflet[1])

    name = leaflet[0].text
    leaflet[0].text = name.upper()
    leaflet[0].set("adjusted", "yes")

xmlDoc.write("./Files chapter 9/drugs_changed.xml")