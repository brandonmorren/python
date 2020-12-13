punctuation_marks = [",  ", ".  ", ";  "]
output_file = open("./Files/hamlet2.txt", "w")
with open("./Files/hamlet.txt") as file:
    line = file.readline()
    while line:
        for character in ',.;:?!':
            line = line.replace(character + '  ', character + ' ')
        output_file.write(line)
        line = file.readline()
output_file.close()