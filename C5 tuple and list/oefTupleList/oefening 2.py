numbers = [9, 17, 25, 4, 12, 7]
combined_list = []

for number in numbers:
    if number % 2 == 0:
        combined_list.insert(0, number)
    else:
        combined_list.append(number)

print(numbers)
print(combined_list)