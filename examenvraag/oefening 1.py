my_address = "De Ruggen 61"
adrress_list = []
guess_list = []
guesses = 0

for i in range(0, len(my_address)-1, 5):
    if (my_address[i] != " ") and (my_address[i] not in adrress_list):
        adrress_list.append(my_address[i].lower())
    adrress_list.sort()

while adrress_list != guess_list:
    letter = input("still " + str((len(adrress_list) - guesses)) + " letters to go: ")
    if (letter in adrress_list) and (letter not in guess_list):
        guess_list.append(letter)
        guess_list.sort()
        guesses += 1
print("yes you did it")