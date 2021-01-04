three_digit_number = int(input("enter a three-digit number: "))

number_one = three_digit_number//100
number_two = (three_digit_number%100) //10
number_three = (three_digit_number%100)%10

print("half = " + str(three_digit_number/2))
print("double = " + str(three_digit_number*2))
print("third power = " + str(three_digit_number**3))
print("thend fold = " + str(three_digit_number*10))
print("the digits are: " + str(number_one) + ", " + str(number_two) + ", " + str(number_three))