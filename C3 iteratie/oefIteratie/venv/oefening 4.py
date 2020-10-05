number_computer = 15
count = 0

player_geuss = int(input("enter a positive number: "))

while player_geuss != number_computer:
    count += 1
    if player_geuss < number_computer:
        print("higher!")
    else:
        print("lower!")
    player_geuss = int(input("enter a positive number: "))

print("you have guessed the number " + str(player_geuss) + " in " + str(count + 1) + " turns")