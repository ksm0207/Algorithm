# 예외처리

# try:    # 실행하고자 하는 코드 예외발생시 실행종료
    # while True:
        # x = int(input("숫자를 나눠보겠습니다"))
        # y = 10 / x
        # print(y)
# except Exception as e:  # 예외가 발생했을떄 발생함
    # print(e, "0은 나눠질수 없습니다")

while True:
    x = [10, 20, 30]
    try:
        index, y = map(int, input("인덱스와 나눌 숫자를 입력하세요").split())
        print(x[index] / y)
    except Exception as error:  # 숫자를 0으로 나누거나 에러 발생시 실행 , 범위를 벗어난 인덱스에 접근시 에러 발생
        print("Exception : ", error)
        
