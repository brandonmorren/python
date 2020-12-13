#r0842912
#kurban yunus
#ITF09

letter = ""
decimal = 0
count = 0

for i in range(1, 6):
    user_input = input(str(i) + ") ")
    letter = user_input[0]
    decimal = int(user_input[1:])
    if ord(letter) != decimal:
        print(letter, "<-->", decimal)
    else:
        count += 1

print(count, "codes were OK")