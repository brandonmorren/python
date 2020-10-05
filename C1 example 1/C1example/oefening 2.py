answer_yes = int(input("how many people voted YES: "))
answer_no = int(input("how many people voted NO: "))
answer_blank = int(input("number of blank votes: "))

total_votes = answer_yes + answer_no + answer_blank;

percent_yes = (answer_yes/total_votes)*100
percent_no = (answer_no/total_votes)*100
percent_blank = (answer_blank/total_votes)*100

print("YES: " + str(percent_yes) + "%")
print("NO: " + str(percent_no) + "%")
print("blank: " + str(percent_blank) + "%")