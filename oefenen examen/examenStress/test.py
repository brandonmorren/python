word = input("Enter a text: ")
count = 1
largest_block = 1
for i in range(len(word)-1):
    if word[i] == word[i+1]:
        count += 1
    else:
        count = 1
    if count > largest_block:
        largest_block = count

print("the length of the largest block in the text is " + str(largest_block))