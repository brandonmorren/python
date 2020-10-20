numbers = (1, 2, 3, 4, 5, 6, 7, 8)
index = 0
print(numbers)
if 4 in numbers:
    for i in range(0,len(numbers)-1):
        if numbers[i] == 4:
            index = i
    print(numbers[index + 1:])
else:
    print("the number 4 does not appear in the tuple")