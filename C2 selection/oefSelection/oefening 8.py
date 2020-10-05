bottles_wine = int(input("how many bottles of wine are there: "))
pizza = int(input("how many pizzas are there: "))

if bottles_wine <= 5 and pizza <= 5:
    print("this is just a stupid party")
else:
    if pizza >= (bottles_wine * 2):
        print("the party is fantastic")
    else:
        print("the party is good")
