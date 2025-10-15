# Problem: Dreamoon and Stairs - https://codeforces.com/problemset/problem/476/A

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


n,m = integers()
min_moves = ceil(n / 2)
ans = -1

k  = ((min_moves + m - 1) // m) * m

if k <= n:
    ans = k
print(ans)