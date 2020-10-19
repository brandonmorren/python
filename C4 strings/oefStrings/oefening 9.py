food = input("what do you eat fort lunch: ")
new_food = ""
if food.count("sandwich") == 2:
    new_food = food[food.find("sandwich"):].replace("sandwich", "")
    print("you have " + new_food + " between your sandwich")
