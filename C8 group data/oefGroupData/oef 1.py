with open("./Files chapter 8/classrooms.txt") as file:
    line = file.readline().rstrip()
    record = line.split(";")
    while line:
        classroom = record[2]
        print(classroom)
        counter = 0
        while line and classroom == record[2]:
            counter += 1
            print("\t", record[1], record[0])
            line = file.readline().rstrip()
            record = line.split(";")
        print("number of students in classroom", classroom, "=", counter)
