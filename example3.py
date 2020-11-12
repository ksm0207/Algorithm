# 문제 : 두 자연수 A와 B가 주어진다
# 조건 1: A+B A-B A*B A/B(나머지) A&B(몫)를 출력하는 프로그램을 작성하시오


def plus(x, y):
    return x + y


def minus(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y


def share(x, y):
    return x % y


one_number = int(input("첫번째 정수 입력 : "))
two_number = int(input("첫번째 정수 입력 : "))

plus_result = plus(one_number, two_number)
print("덧셈 결과 : = ", plus_result)

minus_result = minus(one_number, two_number)
print("뺼셈 결과 : = ", minus_result)

mul_result = multiplication(one_number, two_number)
print("곱셈 결과 : = ", mul_result)

div_result = division(one_number, two_number)
print("나눗셈 결과 : = ", div_result)

share_result = share(one_number, two_number)
print("나머지 결과 : = ", share_result)
