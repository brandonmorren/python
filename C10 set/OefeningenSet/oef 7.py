names = {}
with open("./Files Chapter 10/tasks.csv") as file:
    file.readline()
    line = file.readline().rstrip()
    record = line.split(";")
    while line:
        for i in range(1, 6):
            name = record[i]
            if name in names:
                names[name] += 1
            else:
                names[name] = 1

        line = file.readline().rstrip()
        record = line.split(";")

for item in names:
    print(item, names[item])