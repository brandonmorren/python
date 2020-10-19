new_name = ""
letter = ""
name = input("your name(press enter to stop): ")

print()
print("Menu:")
print(5*"*")
print("U Uppercase")
print("L Lowercase")
print("A Alternate")

choice = input("Make a choice (U-L-A): ")
while choice not in ["U","u","L","l","A","a"]:
    choice = input("Make a choice (U-L-A): ")

if choice in ["U","u"]:
    new_name = name.upper()
elif choice in ["L","l"]:
    new_name = name.lower()
elif choice in ["A","a"]:
    for i in range(0,len(name)):
        if i % 2 == 0:
            letter = name[i].upper()
        else:
            if i % 2 != 0:
                letter = name[i].lower()
        new_name += letter
print(new_name)