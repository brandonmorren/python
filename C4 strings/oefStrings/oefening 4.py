word = input("Enter a word: ")

if (word[0:len(word)]) == (word[-1:0:-1] + word[0]):
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")