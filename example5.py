# 문제
# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D,
# 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

while True:

    student = int(input("성적입력 :  "))

    if student >= 90:
        print("A")
    elif student >= 80 or student >= 89:
        print("B")
    elif student >= 70 or student >= 79:
        print("C")
    elif student >= 60 or student >= 69:
        print("D")
    else:
        print("F")
