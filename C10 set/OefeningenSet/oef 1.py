text = input("enter a text (only letters and numbers): ")
set_numbers = set()
set_letters = set()

for character in text:
    if character != " ":
        if character.isdigit():
            set_numbers.add(character)
        else:
            set_letters.add(character)

print("the numbers: ")
for number in set_numbers:
    print(number)

print("the letters: ")
for letter in set_letters:
    print(letter)