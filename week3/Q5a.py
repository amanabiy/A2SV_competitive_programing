"""
15 min
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
AC -> 29
12 = 2 * 10**0
AAA = 26 ** 3 * 1 + 26 ** 2 * 1 + 26 ** 0 * 1  
"""
n = input()
number = 0
pow = 0
for l in range(len(n) - 1, -1, -1) :
    number += (ord(n[l]) - 64) * 26 ** pow
    pow += 1

print(number)