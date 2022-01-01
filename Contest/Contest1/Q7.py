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
for i in range(len(s) -1 , -1 , -1):
    number += rom[s[i]]
    if i > 0 and rom[s[i]] > rom[s[i - 1]]:
        number -= 2    
print(number)