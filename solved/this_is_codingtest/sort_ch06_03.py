def main():
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
    return None

def solution():
    n = int(input())
    array = []
    for i in range(n):
        input_data = input().split()
        array.append((input_data[0], input_data[1]))

    array = sorted(array, key = lambda student : student[1])
    for student in array:
        print(student[0], end=" ")
    return

if __name__ == "__main__":
    main()
    #solution()