months_days = {"January": 31, "February": 28, "March": 31,
               "April": 30, "May": 31, "June": 30, "July": 31,
               "August": 31, "September": 30, "October": 31,
               "November": 30, "December": 31}

input_month = input("Month (press enter for an overview of all months): ")
if input_month == "":
    for month in months_days:
        print(month, "\t", months_days[month])
else:
    print(months_days.get(input_month, "this month does not exist"))