import random
with open("./Files/table_x.txt", "w") as File:
    number = random.randint(1, 10)
    for i in range(1, 11):
        File.write(str(i) + "x" + str(number) + "=" + str(i*number) + "\n")
