"""
10 min
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
n = int(input())
word = []
while n > 0:
    x = n % 26

    #consider if the letter is Z and remainder is 0
    if x == 0:
        x = 26
        n -= 1
    word.append(chr(int(x + 64)))
    n //= 26
print("".join(reversed(word)))