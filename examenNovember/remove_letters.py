#r0842912
#kurban yunus
#ITF09

list_name = ["Catherine", "Jana", "Leo", "Henry", "Michael"]
new_list_name = []
name = ""
print(list_name)
print()

letter_input = input("Enter the letter you want to remove. press enter if you want to stop: ")
while letter_input != "":
    for i in range(len(list_name)):
        name = list_name[i].replace(letter_input, "")
        new_list_name.append(name)
    list_name = new_list_name
    print(new_list_name)
    new_list_name = []
    letter_input = input("Enter the letter you want to remove. press enter if you want to stop: ")