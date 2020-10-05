count = 0

final_digit = int(input("what final digit do you want to check the numbers on: "))

for i in range(10):
    number = int(input("Enter a number: "))
    if number%10 == final_digit:
        count += 1
print(str(count) + " out of 10 numbers end on " + str(final_digit))