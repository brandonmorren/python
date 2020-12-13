#r0842912
#kurban yunus
#ITF09

lower_limit = int(input("Enter the first number: "))
upper_limit = int(input("Enter the second number: "))
list_numbers = []
change = 0

if lower_limit == upper_limit:
    print("Sorry we can not create a list for you!")
else:
    if upper_limit < lower_limit:
        change = lower_limit
        lower_limit = upper_limit
        upper_limit = change
    for i in range(lower_limit, upper_limit):
        list_numbers.append(i)
    print(list_numbers)