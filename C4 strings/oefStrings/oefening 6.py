word = input("Enter a string: ")

amount_of_groups = len(word) // 3
rest = len(word) % 3
new_word = ""

for i in range(0,(amount_of_groups*3)-1,3):
    new_word += word[i+1] + word[i+2] + word[i]

if rest > 0:
    new_word += word[-rest:]
print(new_word)