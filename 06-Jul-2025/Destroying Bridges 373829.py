# Problem: Destroying Bridges - https://codeforces.com/problemset/problem/1944/A

from functools import reduce
import sys
from math import ceil, floor, gcd, log2
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



t= integer()
for _ in range(t):
    n,k= integers()
    if k >= n - 1:
        print(1)
    else:
        print(n)