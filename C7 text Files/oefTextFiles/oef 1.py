with open("./Files/first_names.txt") as file:
    count = 0
    line = file.readline()
    while line:
        count += 1
        if line != "\n":
            if line.count("z") >= 1 or line.count("Z") >= 1:
                print(line.rstrip())
        line = file.readline()
    print("There are", count, "first names in the file.")