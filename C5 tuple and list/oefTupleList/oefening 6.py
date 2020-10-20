text = input("Enter a text: ")
text_list = []
for i in range(0, len(text)):
    if text[i] != " ":
        if text[i] not in text_list:
            text_list.append(text[i])

text_list.sort()
print(text_list)
print(*text_list)
for letter in text_list:
    print(letter, "\t", end = "")