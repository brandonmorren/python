number = int(input("enter a number: "))

rest = 0
count_zero = 0
count_six = 0

while number != 0:
    rest = number % 10
    number = number // 10
    if rest == 0:
        count_zero += 1
    if rest == 6:
        count_six += 1

print("the number consists of " + str(count_zero) + " zeros and " + str(count_six) + " sixes")
