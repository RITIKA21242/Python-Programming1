# Find runner-up score

n = int(input(" enter number of students: "))
scores = list(map(int, input("enter scores: ").split()))
unique_scores = list(set(scores))
unique_scores.sort(reverse = True)

print(unique_scores[1])