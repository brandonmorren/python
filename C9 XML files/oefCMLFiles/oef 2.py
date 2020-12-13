import xml.etree.ElementTree as ET
xmlDoc = ET.parse("./Files chapter 9/cinemas.xml")
root = xmlDoc.getroot()

print("bioscopen in Antwerpen")
for cinemas in root:
    naam = cinemas.find("naam")
    straat = cinemas.find("straat")
    huisnummer = cinemas.find("huisnummer")
    postcode = cinemas.find("postcode")
    plaats = cinemas.find("district")
    print(naam.text)
    print(straat.text, huisnummer.text)
    print(postcode.text, plaats.text)
    print()

# #dit is een tweede manier
# for cinema in root.findall("bioscoopoverzicht"):
#     naam = cinema.find("naam")
#     straat = cinema.find("straat")
#     huisnummer = cinema.find("huisnummer")
#     postcode = cinema.find("postcode")
#     plaats = cinema.find("district")
#     print(naam.text)
#     print(straat.text, huisnummer.text)
#     print(postcode.text, plaats.text)
#     print()