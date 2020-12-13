import random
output_file = open("./Files/table_x.txt", "w")
number = random.randint(1,10)
for i in range(1,11):
    output_file.write(str(i) + "x" + str(number) + "=" + str(i*number) + "\n")
output_file.close()