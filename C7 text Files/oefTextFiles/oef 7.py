with open("./Files/playlist.txt") as file:
    line = file.readline().rstrip()
    print("playlist")
    while line:
        if line != "\n":
            record = line.split(";")
            print(record[0], "\t", record[1])
        line = file.readline().rstrip()