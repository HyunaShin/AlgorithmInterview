n = int(input())
student_score = dict()
#점수는 101점 까지
coefficients = [0] * 101
for i in range(n):
    student, score = input().split(" ")
    if not student_score.get(int(score)):
        student_score[int(score)] = [student]
    else:
        student_score[int(score)] += [student]
    coefficients[int(score)] +=1

for idx, occured in enumerate(coefficients):
    if student_score.get(idx):
        for value in student_score.get(idx):
            print(value, end = " ")