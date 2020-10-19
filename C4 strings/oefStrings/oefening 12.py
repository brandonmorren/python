word = input("Enter a string: ")
while "*" in word:
    place = word.find("*")
    word = word.replace(word[place - 1:place + 2], "")
print(word)