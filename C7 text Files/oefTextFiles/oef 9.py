with open("./Files/weather_2018 08.csv") as file:
    file.readline() #titel lezen
    highest_temperature = 0
    line = file.readline().rstrip()
    while line:
        if line != "\n":
            record = line.split(";")
            temperature = float(record[1])
            if temperature > highest_temperature:
                highest_temperature = temperature
        line = file.readline().rstrip()
    print("the highest temperature in this period =", highest_temperature, "°C")