# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter,deque
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
for _ in range(t):
    x = integer()
    count = 0
    on = False
    ans = 0
    for i in range(32):
        if x & (1 << i):
            if not on:
                ans += 2 ** i
                on = True
            count += 1
    if count == 1:
        if ans == 1:
            ans += 2
        else:
            ans += 1
    print(ans)

