#For this exercise you use one of your own programs(oef1)
#you write this file to another file with numbering
output_file = open("oef1b.py", "w")
with open("oef 1.py") as file:
    line = file.readline().rstrip()
    counter = 0
    while line:
        counter += 1
        output_file.write(str(counter) + " " + line + "\n")
        line = file.readline().rstrip()
output_file.close()