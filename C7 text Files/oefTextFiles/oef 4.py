with open("./Files/irish_song.txt") as file:
    line = file.readline().rstrip()
    shortest_line_length = len(line)
    shortest_line = line
    while line:
        if line != "\n":
            if len(line) < shortest_line_length:
                shortest_line_length = len(line)
                shortest_line = line
        line = file.readline().rstrip()
    print("the shortest line has", shortest_line_length, "characters")
    print(shortest_line)