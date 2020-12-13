all_stock = []
stock = []
counter = 0

with open("./Files/stock1.txt") as file1:
    file1.readline()
    line = file1.readline().rstrip()
    while line:
        record = line.split(";")
        all_stock.append(record)
        line = file1.readline().rstrip()

with open("./Files/stock2.txt") as file2:
    file2.readline()
    line = file2.readline().rstrip()
    while line:
        record = line.split(";")
        all_stock.append(record)
        line = file2.readline().rstrip()

with open("./Files/stock3.txt", "w", encoding="utf-8") as file3:
    all_stock.sort()
    file3.write("item number;stock \n")
    while counter < len(all_stock):
        item = all_stock[counter][0]
        print(item, "\t", end="")
        sum = 0
        while counter < len(all_stock) and all_stock[counter][0] == item:
            sum += int(all_stock[counter][1])
            counter += 1
        file3.write(item + ";" + str(sum) + "\n")