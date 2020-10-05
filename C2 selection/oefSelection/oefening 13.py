choice_of_computer = "rock"
choice_of_player = input("what do you choose: paper, rock or scissors? ")

if (choice_of_computer == "rock" and choice_of_player == "scissors") or (choice_of_computer == "scissors" and choice_of_player == "paper") or (choice_of_computer == "paper" and choice_of_player == "rock"):
    print("computer wins")
elif choice_of_computer == choice_of_player:
    print("nobody wins")
else:
    print("player wins")