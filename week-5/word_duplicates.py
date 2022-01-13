#!/usr/bin/env python3
"""
remove a substring from 
a given string
"""


def remove_sub(word: str, sub: str) -> str:
    res = []
    for letter in word:
        if letter != sub[-1]:
            res.append(letter)
        else:
            length = len(sub) - 2
            for l in range(length, -1, -1):
                if res and res[-1] == sub[l]:
                    res.pop()
                else:
                    for i in range(l+1, len(sub)):
                        res.append(sub[i])
    return res

if __name__ == "__main__":
    word = input()
    sub = input()
    print (remove_sub(word, sub))