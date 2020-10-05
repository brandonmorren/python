year_of_birth = int(input("enter your year of birth: "))

this_year = 2020
age = this_year - year_of_birth

print("your age = " + str(age))

if age >= 18:
    print("so you are an adult.")
else:
    print("you are not an adult yet.")