with open("./Files/first_names.txt") as file:
    list_names = file.readlines()
    for i in range(len(list_names)-1, -1, -1):
        list_names[i] = list_names[i].replace("\n", "")
        print(list_names[i])
