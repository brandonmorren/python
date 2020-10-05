age_of_you = int(input("how old are you: "))
age_of_father = int(input("how old is your father: "))

if (age_of_you * 2) < age_of_father:
    count = 0
    while (age_of_you * 2) != age_of_father:
        count += 1
        age_of_you += 1
        age_of_father += 1
    print("within " + str(count) + " years your father will have twice your age")
    print("your father will be " + str(age_of_father) + " and you will be " + str(age_of_you))
else:
    print("the situation is no longer possible for your ages")

