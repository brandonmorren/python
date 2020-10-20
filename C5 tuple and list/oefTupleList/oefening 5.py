# numbers = [42, 18, 0, 37, 0, 2, 19, 20, 5, 14]
numbers = [42, 18, 17, 0, 2, 19, 0]
print(numbers)
for index in range(len(numbers)-1):
    if numbers[index] == 0:
        # search largest_odd
        largest_odd = 0
        for i in range(index+1, len(numbers)-1):
            if numbers[i] > largest_odd and numbers[i] % 2 != 0:
                largest_odd = numbers[i]
        numbers[index] = largest_odd
print(numbers)