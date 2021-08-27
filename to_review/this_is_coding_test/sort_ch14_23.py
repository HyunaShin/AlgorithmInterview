# 파이썬에서는 튜플을 원소로하는 리스트가 있을 때, 그 리스트를 정렬하면 기본적으로
# 각 튜플을 구성하는 원소의 순서에 맞게 정렬되는 특징이 있다.

def main():
    n = int(input())
    students = []
    for _ in range(n):
        students.append(tuple(input().split(" ")))

    students.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

    for student in students:
        print(student[0])
    return None




def solution():
    n = int(input())
    students = []

    for _ in range(n):
        students.append(input().split(" "))

    #[정렬 기준]
    # 1) 두번째 원소(국어점수)를 기준으로 내림차순 정렬
    # 2) 두번째 원소(국어점수)가 같은 경우, 세번째 원소(영어점수)를 기준으로 오름차순 정렬
    # 3) 세번째 원소(영어점수)가 같은 경우, 네번째 원소(수학점수)를 기준으로 내림차순 정렬
    # 4) 네번째 원소(수학점수)가 같은 경우, 첫번째 원소(이름)를 기준으로 오름차순 정렬

    students.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

    for student in students:
        print(student[0])
    return None

if __name__ == "__main__":
    main()