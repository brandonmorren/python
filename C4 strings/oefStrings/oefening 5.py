count_triple = 0

word = input("Enter a word: ")

for i in range(0, len(word)-4):
    if word[i] == word[i+1] == word[i+2]:
        count_triple += 1

if count_triple > 1:
    print("there are " + str(count_triple) + " triples in this text")
elif count_triple == 1:
    print("there is " + str(count_triple) + " triple in this text")
elif count_triple == 0:
    print("there are no triples in this text")