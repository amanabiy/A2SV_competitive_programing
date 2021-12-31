# 5 min
s = input()
rom = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
number = 0
for i in range(len(s)):
    number += rom[s[i]]
    
print(number)