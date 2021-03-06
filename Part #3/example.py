# 문제
# 상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다.
#  설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
#
# 상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 예를 들어, 18킬로그램 설탕을 배달해야 할 때,
# 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.
#
# 상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)
#
# 출력
# 상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.
w_count = 0
suggar = 0
suggar03 = 3
suggar05 = 5
num = int(input("설탕 Kg 입력 : "))
print(f"사장님: 오늘은 {num} Kg 만큼 배달 해야 합니다 !!")
print("상근 : 설탕봉지 무게량", suggar03, "Kg", suggar05, "Kg")
while True:
    suggar += 1
    w_count += 1
    print("suggar = ", suggar)
    num = num - suggar03
    print(f"num - suggar03 = {num}")
    print(f"=======While 문 {w_count}번 실행 ========")

    if num % suggar05 == 0:  # num / 5 == 0 으로 떨어질때
        print("num = ", num)
        suggar = suggar + (num // suggar05)  # 1 + ()
        print("Result = ", suggar)
        break
    else:
        if num < 0:
            print(-1)
            break
