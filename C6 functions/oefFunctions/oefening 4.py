def generate_list(amount):
    import random
    list_numbers = []
    for i in range(0, amount):
        random_numbers = random.randint(1, 6)
        list_numbers.append(random_numbers)
    return list_numbers


choosen_amount = int(input("how many dices do you want to roll? "))

my_threw = generate_list(choosen_amount)
print("you threw: " + str(my_threw))

count = 1

while (choosen_amount * [choosen_amount]) != my_threw:
    my_threw = generate_list(choosen_amount)
    print("you threw: " + str(my_threw))
    count += 1
print("you threw poker after " + str(count))