# 문제
# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.
#
# 출력
# 1부터 n까지 합을 출력한다.

number = 1
num = int(input("정수 입력 : "))

for i in range(num):
    number += i
print(f" 1 부터 {num} 까지의 합은 = {number + i} 입니다")

