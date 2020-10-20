first_list = [2, 4, 5, 9]
print(first_list)

new_list = []
for i in range(len(first_list)*2-1):
    new_list.append(0)
new_list.append(first_list[-1])

print(new_list)