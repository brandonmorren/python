first_name = input("enter first name: ")
second_name = input("enter second name: ")

print("before changing:", first_name,second_name)

# help is een hulpvariable om tijdelijk een gegeven op te slagen
help = first_name
first_name = second_name
second_name = help

# dit gaat alleen in python,
# first_name ,second_name = second_name, first_name

print("after changing:", first_name,second_name)