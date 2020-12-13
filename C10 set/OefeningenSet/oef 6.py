animals = {"dog": "barks", "cat": "meows", "bird": "flies"}
correct_answer = 0

for item in animals:
    input_user = input("what is de sound of a " + item + ": ")
    if input_user == animals[item]:
        correct_answer += 1

print("you have", correct_answer, "correct answers")