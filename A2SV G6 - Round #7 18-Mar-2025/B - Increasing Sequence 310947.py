# Problem: B - Increasing Sequence - https://codeforces.com/gym/596141/problem/B

#© @haymi

import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
 
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
    n = integer()
    nums = List()

    arr = []
    last_b = 0
    for i in range(n):
        candidate = last_b + 1
        if candidate == nums[i]:
            candidate += 1
        arr.append(candidate)
        last_b = candidate
    print(arr[-1])
