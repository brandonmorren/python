with open("./Files chapter 8/courses.csv") as file:
    file.readline().rstrip()
    line = file.readline().rstrip()
    record = line.split(";")
    while line:
        student_number = record[3]
        last_name = record[4]
        first_name = record[5]
        print(student_number,last_name,first_name, sep=";", end="")
        while line and record[3] == student_number:
            print(";" + record[1] + " (" + record[2] + ")", end="")
            line = file.readline().rstrip()
            record = line.split(";")
        print()