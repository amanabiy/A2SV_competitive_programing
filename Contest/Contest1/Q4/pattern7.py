"""
6 min
##  ##  ##
  ##  ##
##  ##  ##
"""
n = int(input())
for i in range(1, n+1):
    if i % 2 != 0:
        for j in range(n):
            print("##  ", end="")
        print()
    else:
        for j in range(n-1):
            print("  ##", end="")
        print()