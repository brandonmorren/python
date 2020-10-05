number_one = int(input("number 1: "))
number_two = int(input("number 2: "))
number_three = int(input("number 3: "))

if number_one + number_two == number_three or number_one + number_three == number_two or number_two + number_three == number_one:
    print("this works")
else:
    print("this doesn't work")