color = input("what is your favourite color: ")

print(color[0] + color[2])
print("this colour consist of " + str(len(color)) + " letters")
print()
for i in range(0, len(color)):
    letter = color[i]
    print(letter," = ",ord(letter))
print()
for y in range(0, len(color)):
    if y % 2 == 0:
        print("#" + color[y] + "#")
    else:
        if y % 2 != 0:
            print("**"+ color[y] + "**")