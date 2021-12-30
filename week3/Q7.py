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
    if len(s) == 2:
        if s[i]=="I" and s[i + 1] == "V":
            number+= 4
        if s[i]=="I" and s[i + 1] == "X":
            number+=9
        break
    if i < len(s) - 1:
        if s[i]=="I" and s[i + 1] == "V":
            number+= 4
        if s[i]=="I" and s[i + 1] == "X":
            number+=9
        else:
            number += rom[s[i]]
    else:
        number += rom[s[i]]
    
print(number)