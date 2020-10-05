number_one = int(input("number 1 (0, 1 or 2): "))
number_two = int(input("number 2 (0, 1 or 2): "))
number_three = int(input("number 3 (0, 1 or 2): "))

result = 0

if number_one == number_two == number_three == 2:
    result = 10
elif number_one == number_two == number_three != 2:
    result = 5
elif number_two == number_three != number_one:
    result = 1
else:
    result

print(str(result))