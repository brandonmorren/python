import xml.etree.ElementTree as ET
xmlDoc = ET.parse("./Files chapter 9/jobs.xml")
root = xmlDoc.getroot()

count = 1
for company in root.iter("company"):
    for vacancy in company.iter("vacancy"):
        if vacancy[0].get("group") == "IT":
            print(str(count) + ".", "\t", "position:", "\t", vacancy[0].text)
            print("\t", "company:", "\t", company[0].text)
            print("\t", "contact:", "\t", company[1][1].text)
            print()
            count += 1