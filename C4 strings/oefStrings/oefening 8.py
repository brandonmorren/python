word = input("enter a word: ")
place = 0
text = ""

if "in" in word:
    place = word.find("in")
    if place in [0,1]:
        text = "'in' appears in the first or second place"
    else:
        text = "'in' appears in the word, but not in front"
else:
    text = "this word does not contain 'in'"

print(text)

