import xml.etree.ElementTree as ET

with open("./Files chapter 9/songs.txt") as file:
    artist_list = []
    song_list = []

    line = file.readline().rstrip()
    record = line.split(";")

    while line:
        artist_list.append(record[0])
        song_list.append(record[1])

        line = file.readline().rstrip()
        record = line.split(";")


root = ET.Element("compilation")
for i in range(len(artist_list)):
    Track = ET.Element("Track")

    artist = ET.Element("artist")
    artist.text = artist_list[i]
    Track.append(artist)

    song = ET.Element("song")
    song.text = song_list[i]
    Track.append(song)

    root.append(Track)

tree = ET.ElementTree(root)
tree.write("./Files chapter 9/songs.xml", encoding="utf-8", xml_declaration=True)
