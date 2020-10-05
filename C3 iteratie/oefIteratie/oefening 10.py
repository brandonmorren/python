price = 0
price_discount = 0

for i in range(1,5):
    print("information for member " + str(i))
    name = input("Name: ")
    age = int(input("Age:"))
    years_of_membership = int(input("Member for how many years: "))

    if age < 12:
        price = 20
        if years_of_membership >= 5:
            price = price * 0.9
    elif 12 <= age <= 18:
        price = 50
        if years_of_membership >= 5:
            price = price * 0.9
    elif age > 18:
        price = 95
        if years_of_membership >= 5:
            price = price * 0.9

    print("member fee for " + name + " = " + str(price))
    print()