with open("./Files/contacts.csv") as file:
    line = file.readline().rstrip()
    list_girls = []
    list_boys = []
    while line:
        if line != "\n":
            record = line.split(";")
            if record[3] == "M":
                name = record[0] + " " + record[1]
                list_boys.append(name)
            elif record[3] == "V":
                name = record[0] + " " + record[1]
                list_girls.append(name)
        line = file.readline().rstrip()

    list_boys.sort()
    list_girls.sort()

    print(len(list_girls), "girls:")
    for girls in list_girls:
        print("\t", girls)
    print(len(list_boys), "boys:")
    for boys in list_boys:
        print("\t", boys)