with open("./Files chapter 8/sponsors.txt") as file:
    list_sort = file.readlines()

list_sort.sort()
counter = 0
count_taxes = 0
line = list_sort[counter]
record = line.split("*")
while counter < len(list_sort):
    number = record[0]
    print(number, "\t", record[1], record[2].ljust(10), "\t", end="")
    amount = 0
    while counter < len(list_sort) and record[0] == number:
        amount += int(record[3])
        counter += 1
        if counter < len(list_sort):            #if is nodig om te controleren om te zien of je niet uit uw index gaat
            line = list_sort[counter]
            record = line.split("*")
    if amount > 40:
        print(amount, "**")
        count_taxes += 1
    else:
        print(amount)
print("there are", count_taxes, "tax certificates to be sent")