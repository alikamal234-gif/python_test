scores = [45, 12, 78, 34, 90, 23, 67, 56, 89, 10]
print(scores)
copie_scores = scores.copy()

scores.sort()
copie_scores.sort(reverse=True)
print(scores, copie_scores , scores[-3:])

