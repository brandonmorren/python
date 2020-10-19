word = input("Enter a text: ")
count = 0
largest_block = 0
for i in range(0, len(word)-2):
    if word[i] == word[i+1]:
        count += 1
        if word[i+1] != word[i+2]:
            if largest_block < count:
                largest_block = count
                count = 0

print("the length of the largest block in the text is " + str(largest_block + 1))
