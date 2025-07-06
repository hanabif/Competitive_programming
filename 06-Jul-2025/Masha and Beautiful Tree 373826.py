# Problem: Masha and Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

#© @haymi

import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter
from bisect import bisect_left,bisect_right
from itertools import accumulate

def string(): return sys.stdin.readline().strip()
def integer(): return int(sys.stdin.readline().strip())
def integers(): return map(int, sys.stdin.readline().strip().split())
def List(): return list(map(int, sys.stdin.readline().strip().split()))
def strings(): return map(str, sys.stdin.readline().strip().split())
def stringList(): return list(map(str, sys.stdin.readline().strip().split()))
def Matrix(n): return list(list(map(int, sys.stdin.readline().strip().split())) for i in range(n))

t = integer()
while t:
    t-=1
    n = integer()
    nums = List()

    def mergeSort(arr):
        if len(arr) == 1:
            return (arr , 0)
        
        mid = len(arr)// 2

        left , left_c = mergeSort(arr[:mid])
        right, right_c = mergeSort(arr[mid:])

        ans , count = merge(left,right)
        return (ans , count + left_c + right_c)

    def merge(left , right):
        if left[0] > right[0]:
            return (right + left , 1)
        else:
            return (left + right, 0 )
        

    res, count = mergeSort(nums)
    
    if res == sorted(nums):
        print(count)
    else:
        print(-1)