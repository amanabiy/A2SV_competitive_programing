#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    for index in range (n - 1, -1, -1):
        key = arr[index]
        if index != 0:
            # print("index: {}".format(index))
            temp: int = index - 1
            # print("temp: {}".format(temp))
            count: int = 0
            while arr[temp] > key and temp >= 0:
                arr[temp + 1] = arr[temp]
                for i in range(n):
                    print(arr[i], end="")
                    if(i != n - 1):
                        print(" ",end="")
                    else:
                        print("")
                temp -= 1
                count += 1
            if count != 0:
                arr[temp + 1] = key
                for i in range(n):
                    print(arr[i], end="")
                    if(i != n - 1):
                        print(" ",end="")
                    else:
                        print("")
                    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
