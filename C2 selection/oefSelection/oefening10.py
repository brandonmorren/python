number_one = int(input("first number: "))
number_two = int(input("second number: "))

text = "they are not ok"

if (30 <= number_one <= 40 and 30 <= number_two <= 40) or \
        (number_one in [65, 72, 83, 90] and number_one in [65, 72, 83, 90]):
    text = "both numbers are ok"

print(text)