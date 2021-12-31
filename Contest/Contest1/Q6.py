# 5 min
num = list(map(int, input().split()))
for i in range(len(num)):
    for j in range(len(num)-1):
        if num[j] == 0:
            num[j], num[j + 1] = num[j + 1], num[j]

print(num)