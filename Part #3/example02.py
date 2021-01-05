# 문제
# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
#
# 예를 들어, 서로 다른 9개의 자연수
#
# 3, 29, 38, 12, 57, 74, 40, 85, 61
#
# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.
#
# 입력
# 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.
#
# 출력
# 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.


num = int(input("서로 다른 자연수를 N만큼 입력하세요 : "))
max_value = []


def find_max_value():

    print(f"{num} 만큼 입력하셨습니다")
    print("=" * 5)
    for i in range(num):
        value = int(input())
        max_value.append(value)
    print("=" * 5)

    print(f"최대값= {max(max_value)} / 위치= {max_value.index(max(max_value))+1} 번째에 있습니다 ")


find_max_value()

