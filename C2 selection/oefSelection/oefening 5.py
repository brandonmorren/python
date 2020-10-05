number = int(input("enter a number: "))

if number <= 0:
    print("negative numbers will not be tested")
else:
    test_number = int(input("what final digit do you want to test with: "))
    if test_number == (number % 10):
        print(str(number) + " ends with " + str(test_number))
    else:
        print(str(number) + " does not end with " + str(test_number))