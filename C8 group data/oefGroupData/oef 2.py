with open("./Files chapter 8/courses.csv") as file:
    file.readline().rstrip()
    line = file.readline().rstrip()
    record = line.split(";")
    list_students = []
    student = ""
    while line:
        student_number = record[3]
        last_name = record[4]
        first_name = record[5]
        student = student_number + ";" + last_name + ";" + first_name
        while line and record[3] == student_number:
            student += ";" + record[1] + " (" + record[2] + ")"
            line = file.readline().rstrip()
            record = line.split(";")
        student += "\n"
        list_students.append(student)

with open("./Files chapter 8/students.csv", "w") as file:
    file.writelines(list_students)