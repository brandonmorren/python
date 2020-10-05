count = 0
product = 1

number = int(input("enter a number, stop by entering a zero: "))

while number != 0:
    count += 1
    product *= number
    number = int(input("enter a number, stop by entering a zero: "))

print("the product of the " + str(count) + " numbers is " + str(product))