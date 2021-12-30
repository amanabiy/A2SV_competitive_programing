n = int(input())
# with out loop
# 10 min
# let = '#' * (i - 1)
# print((let + ' ') * i)
# print((let + ' ') * i)

# with loop
for i in range(2):
    let =''
    for i in range(0, n-1):
        let += '#' 
    printable = ''
    for i in range(n):
        printable += let + " "
    print(printable)