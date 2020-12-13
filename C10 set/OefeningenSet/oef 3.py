set_local = set()

with open("./Files Chapter 10/local_booking.txt") as file:
    line = file.readline().rstrip()
    record = line.split(";")
    while line:
        set_local.add(record[3])
        line = file.readline().rstrip()
        record = line.split(";")

print("classrooms:")
for local in set_local:
    print(local)