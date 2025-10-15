# student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68,
#                   199, 78, 65, 89, 86, 55, 91, 64, 89]
# print(range(1, 10))
#
# total_score = sum(student_scores)
# print(total_score)
#
# max_number = max(student_scores)
# print(max_number)
#
# min_number = min(student_scores)
# print(min_number)

student_scores = [8, 65, 89, 86, 55, 91, 64, 89]
max_score = 0
min_score = student_scores[0]

for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)

for minScore in student_scores:
    if minScore < min_score:
        min_score = minScore
print(min_score)


