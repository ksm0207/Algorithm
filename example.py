# 재귀함수
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)


# 5(n-1) , 4(n-1) . . .

print(fact(5))

