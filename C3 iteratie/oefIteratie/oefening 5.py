number = int(input("enter a number: "))
if number != 0:
    smallest_number = number
    highest_number = number
    difference = 0
    while number != 0:
        if number < smallest_number:
            smallest_number = number
        if number > highest_number:
            highest_number = number
        difference = highest_number - smallest_number
        number = int(input("enter a number: "))
    print("the difference between the largest number " + str(highest_number) + " and the smallest number " + str(smallest_number) + " = " + str(difference))
else:
    print("no numbers entered")