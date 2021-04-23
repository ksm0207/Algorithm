a = [1, 2, 3, 4, 5, 7]

print(a[2], end="")  # "" 으로하면 줄바꿈 x
print(a[3])
print(a[0:2])

# 출력 값
# 34
# [1,2]

print(a[2], end="\n")  # "\n" end 옵션설정
print(a[3])
print(a[0:2])

# 출력 값
# 3
# 4
# [1,2]

print(a[2], end="ABC")  # ABC 문자열넣기
print(a[3])
print(a[0:2])

# 출력 값
# 3ABC4
# [1,2]
