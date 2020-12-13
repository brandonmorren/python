import xml.etree.ElementTree as ET
xmlDoc = ET.parse("./Files chapter 9/drugs.xml")
root = xmlDoc.getroot()

# for child in root:
#     print(child.tag, child.attrib)


# print("root[1].tag:", root[1].tag)
# print("root[0][3].tag:", root[0][3].tag)
# print("root[0][3].text:", root[0][3].text)
# print("root[1][0].text:", root[1][0].text)
# print("root[1][1][1].text:", root[1][1][1].text)
# print("root[2][3].text:", root[2][3].text)


# for leaflet in root.iter('leaflet'):
#     print(leaflet[0].text, ':', leaflet[3].text)


# # Voorbeeld met iter en nummeren van kindknopen
# for leaflet in root.iter('leaflet'):
#     print(leaflet[0].text)
#     print('\t',leaflet[2].text)
#     print('\t','pharmaceutical forms:')
#     for form in leaflet[1]:
#         print('\t\t',form.text)


# # Voorbeeld met iter en find
# for leaflet in root.iter('leaflet'):
#     reason = leaflet.find('group')
#     name_drug = leaflet.find('name')
#     print(name_drug.text)
#     print('\t', reason.text)
#     print('\t','pharmaceutical forms:')
#     for form in leaflet.find('pharmaceutical_forms'):
#         print('\t\t', form.text)


# # Uitgebreider voorbeeld met iter en find
# for leaflet in root.iter('leaflet'):
#     reason = leaflet.find('group')
#     if reason.text == 'pain medication':
#         name_drug = leaflet.find('name')
#         print(name_drug.text)
#         for form in leaflet.find('pharmaceutical_forms'):
#             print('\t\t', form.text)


# # Voorbeeld met findall ipv iter
# for leaflet in root.findall('leaflet'):
#     reason = leaflet.find('group')
#     if reason.text == 'pain medication':
#         name_drug = leaflet.find('name')
#         print(name_drug.text)
#         for form in leaflet.find('pharmaceutical_forms'):
#             print('\t\t', form.text)


# # Voorbeeld dat duidelijk maakt dat iter ook toelaat om in heel de boom te gaan kijken
# for info in root.iter('form'):
#     print('*',info.text)