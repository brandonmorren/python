number_one = int(input("number 1: "))
number_two = int(input("number 2: "))
number_three = int(input("number 3: "))

smallest_number = number_one

if number_two < smallest_number:
    smallest_number = number_two
if number_three < smallest_number:
    smallest_number = number_three

print("the smallest number is: " + str(smallest_number))
