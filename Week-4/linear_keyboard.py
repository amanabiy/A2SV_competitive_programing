#!/usr/bin/env python3

def time(keyBoard, word):
    """time to write a word"""
    distance = 0
    x = 1
    letters = {}
    for letter in keyBoard:
        letters[letter] = x
        x += 1
    for i in range(len(word) - 1):
        distance += abs(letters[word[i]] - letters[word[i + 1]])
    return distance
if __name__ == "__main__":
    for _ in range(int(input())):
        keyBoard = input()
        word = input()
        print (time(keyBoard, word))