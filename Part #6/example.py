# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
#
# 출력
# 주어진 수들 중 소수의 개수를 출력한다.


num_input = int(input())
numbers = map(int, input().split())
result = 0

for num in numbers:
    value = 0
    if num > 1:
        for i in range(2, num):  # 2부터 n-1까지
            if num % i == 0:
                value += 1  # 2부터 n-1까지 나눈 몫이 0이면 error가 증가
        if value == 0:
            result += 1  # error가 없으면 소수.
print(result)
