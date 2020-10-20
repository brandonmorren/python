print("enter the scores for the test. Use -1 if you want to finish")
list_scores = []
score = float(input("score: "))
while score != -1:
    list_scores.append(score)
    score = float(input("score: "))
list_scores.sort()
average = sum(list_scores) / len(list_scores)
print("these scores (ordered):", list_scores)
print("the average of these", len(list_scores), "scores =", average)
