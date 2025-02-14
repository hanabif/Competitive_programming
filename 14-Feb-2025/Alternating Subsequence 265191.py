# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

#© @haymi

import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter
 
def string(): return sys.stdin.readline().strip()
def integer(): return int(sys.stdin.readline().strip())
def integers(): return map(int, sys.stdin.readline().strip().split())
def List(): return list(map(int, sys.stdin.readline().strip().split()))
def strings(): return map(str, sys.stdin.readline().strip().split())
def stringList(): return list(map(str, sys.stdin.readline().strip().split()))
def Matrix(n): return list(list(map(int, sys.stdin.readline().strip().split())) for i in range(n))

t= integer()

while t:
    t-=1
    size = integer()
    arr = List()
    
    left = 0
    ans = 0

    for right in range(1, size):
        if (arr[left] > 0 and arr[right] < 0) or (arr[left] < 0 and arr[right] > 0):
            ans+= max(arr[left:right])
            left=right
    ans+= max(arr[left:])
    print(ans)
