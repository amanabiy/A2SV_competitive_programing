"""
10 min
*             *
* *         * *
* * *     * * *
* * * * * * * *
"""
n = int(input())
x = n * 2
for i in range(1, n+1):
    print('*' * i, end="")

    print(' ' * (x - (2 * i)), end="")
    print('*' * i)

