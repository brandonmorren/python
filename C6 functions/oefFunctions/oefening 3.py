def press_square(number, character):
    for i in range(0, number):
        print(character*number)


choosen_character = input("which character must be used to form the lines (enter = stop): ")
choosen_number = int(input("number of characters per line = number of lines = "))

press_square(choosen_number,choosen_character)