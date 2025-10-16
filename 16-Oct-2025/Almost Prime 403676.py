# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

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

n = integer()
ans = 0
for i in range(n+1):
    d = 2
    res = set()
    while d * d < i:
        while i % d == 0:
            res.add(d)
            i//=d
        d += 1
    if i > 1:
        res.add(i)
    if len(res) == 2:
        ans += 1
print(ans)
