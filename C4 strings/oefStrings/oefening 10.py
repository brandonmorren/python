new_text = ""

for i in range(1, 6):
    word = input("enter word " + str(i) + ": ").capitalize()
    new_text = word + " " + new_text

print("the words in reverse order:")
print(new_text)