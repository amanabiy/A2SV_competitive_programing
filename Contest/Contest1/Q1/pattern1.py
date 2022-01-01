"""
10 min
      *
    * * *
  * * * * *
* * * * * * *
"""
n = int(input())
space = n  * 2
x = 1
for i in range(n):
    print(' ' * space, end="")
    space -= 1
    print('*' * x)
    x += 2
