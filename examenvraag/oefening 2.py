def count_code(str):
    count = 0
    word = ""

    while "co" in str:
        index = str.find("co")
        if len(str) >= 4 and "e" == str[index + 3]:
            word = "co" + str[index + 2] + str[index + 3]
            count += 1
            str = str[0:index] + str[index + 4:]
        else:
            str = str[0:index] + str[index + 2:]
        print(str)
    return count


print(count_code("coe"))