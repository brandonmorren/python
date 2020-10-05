current_hour = int(input("enter the current hour: "))
waiting_time = int(input("how long dou you want to wait: "))

alarm_time = (current_hour + waiting_time) %24

print("the alarm will soun at " + str(alarm_time) + "h")