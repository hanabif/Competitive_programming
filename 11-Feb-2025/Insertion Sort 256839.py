# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

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
    for i in range(1,n):
        temp=arr[i]
        
        j=i-1
        while j>=0 and temp<arr[j]:
            arr[j+1]=arr[j]
            print(*arr)
            
            j-=1
        arr[j+1]=temp
    print(*arr)
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
