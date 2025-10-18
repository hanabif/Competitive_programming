# Problem: Limited Repainting - https://codeforces.com/contest/2070/problem/C

from functools import reduce
import sys
from math import ceil, floor, gcd, log2
from collections import defaultdict, Counter,deque
from bisect import bisect_left,bisect_right
from itertools import accumulate
from functools import lru_cache

def string(): return sys.stdin.readline().strip()
def integer(): return int(sys.stdin.readline().strip())
def integers(): return map(int, sys.stdin.readline().strip().split())
def List(): return list(map(int, sys.stdin.readline().strip().split()))
def strings(): return map(str, sys.stdin.readline().strip().split())
def stringList(): return list(map(str, sys.stdin.readline().strip().split()))
def Matrix(n): return list(list(map(int, sys.stdin.readline().strip().split())))

def min_penality(n,k,s,a):
    def can(x):
        ops = 0
        i = 0
        while i < n:

            if a[i] <= x:
                i += 1
                continue

            if s[i] == 'B':
                ops += 1
                while i < n and (s[i] != 'R' or a[i] <= x):
                    i += 1
            else:
                i += 1
        return ops <= k
    
    left , right = 0 , max(a)
    ans = right
    while left <= right:
        mid = (left + right) // 2
        if can(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans 


t = integer()
for _ in range(t):
    n,k = integers()
    s = string()
    a = List()
    print(min_penality(n,k,s,a))

