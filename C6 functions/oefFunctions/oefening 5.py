def count_upper_lower(str):
    capitals = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    lowercase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    count_capitals = 0
    count_lowercase = 0

    for letter in str:
        if letter != " ":
            if letter in capitals:
                count_capitals += 1
            elif letter in lowercase:
                count_lowercase += 1
    return [count_capitals, count_lowercase]


your_string = input("set your password (at least 2 uppercase and 3 lowercase letters): ")
while count_upper_lower(your_string)[0] != 2 and count_upper_lower(your_string)[1] != 3:
    your_string = input("set your password (at least 2 uppercase and 3 lowercase letters): ")
