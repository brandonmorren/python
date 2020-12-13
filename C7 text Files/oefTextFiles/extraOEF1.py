def read_month(input_month):
    if input_month == 8:
        file = open("./Files/weather_2018 08.csv")
    elif input_month == 10:
        file = open("./Files/weather_2018 10.csv")

    file.readline()  #titel lezen
    line = file.readline().rstrip()
    highest_temperature = 0
    first_period = line.split(";")[0]
    last_period = ""
    period = ""

    while line:
        if line != "\n":
            last_period = line.split(";")[0]
            record = line.split(";")
            temperature = float(record[1])
            if temperature > highest_temperature:
                highest_temperature = temperature
                period = line.split(";")[0]
        line = file.readline().rstrip()
    file.close()
    return [first_period, last_period, highest_temperature, period]


month = int(input("Choose a month: "))
while month > 1 and month > 12:
    month = int(input("Choose a month: "))

if month not in [8, 10]:
    print("no data available")
else:
    values = read_month(month)
    print()
    print("period:", "\t", values[0], "-", values[1])
    print(6*"-")
    print("the highest temperature in this period =", values[2], "°C")
    print("this temperature was measured at", values[3][-5:], "on", values[3][:9])