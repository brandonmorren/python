with open("./Files/first_names.txt") as file:
    count = 0
    count_z = 0
    line = file.readline()
    while line:
        count += 1
        if line != "\n":
            if line.count("z") >= 1 or line.count("Z") >= 1:
                print(line.rstrip())
                count_z += 1
        line = file.readline()
    print("There are", count, "first names in the file.")
    print(count_z, "names with letter z")