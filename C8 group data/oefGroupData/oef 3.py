with open("./Files chapter 8/weather_2018 10.csv") as file:
    file.readline().rstrip()
    line = file.readline().rstrip()
    record = line.split(";")
    print("average temperatures: ")
    while line:
        date = record[0][:10]
        print(date, "\t", end="")
        counter = 0
        sum = 0
        average = 0
        while line and record[0][:10] == date:
            counter += 1
            sum += float(record[1])
            line = file.readline().rstrip()
            record = line.split(";")
        average = sum / counter
        print("number of measurements =", counter, "\t", "average =", '{:.4}'.format(average))
    print(">"*60)