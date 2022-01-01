"""
7 min
  1
 121
12321
"""
n = int(input())
printed = []
for i in range(1, n+1):
    for j in range(n-i):
        print("  ", end="")
    for j in range(1, i+1):
        print("{} ".format(j), end="")
    for j in range(i -1, 0, -1):
        print("{} ".format(j), end="")
    print()
for i in range(n, 0, -1):
    for j in range(n-i):
        print("  ", end="")
    for j in range(1, i + 1):
        print("{} ".format(j), end="")
    for j in range(i-1, 0, -1):
        print("{} ".format(j), end="")
    print()