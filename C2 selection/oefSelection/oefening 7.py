first_number = int(input("first number: "))
second_number = int(input("second number: "))

answer =0

if first_number < 0:
    first_number = - first_number
if second_number < 0:
    second_number = - second_number

if first_number == second_number:
    answer = 0
else:
    if first_number%5 == 0 and second_number%5 == 0:
        if first_number < second_number:
            answer = first_number
        else:
            answer = second_number
    else:
        if first_number > second_number:
            answer = first_number
        else:
            answer = second_number
print("the answer of the numbers " +
          str(first_number) + " and " + str(second_number) + " = "
          + str(answer))