word = input("enter a string: ")
followed_by_y = True

for i in range(0, len(word) - 1):
    if (word[i] == "x") and ("y" in word[i:]):
        followed_by_y = True
    else:
        if (word[i] == "x") and ("y" not in word[i:]):
            followed_by_y = False

if followed_by_y:
    print("in this text every x is followed by a y")
else:
    print("in this text not every x is followed by a y")