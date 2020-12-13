import random
number = random.randint(1,10)
with open("./Files/wish" + str(number) + ".txt") as file:
    print("wish", number)
    print()
    line = file.readline().rstrip()
    while line:
        if line != "\n":
            print(line)
        line = file.readline().rstrip()
