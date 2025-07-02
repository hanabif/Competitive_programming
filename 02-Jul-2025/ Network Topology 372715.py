# Problem:  Network Topology - https://codeforces.com/problemset/problem/292/B

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

n,m = integers()
deg = [0]* (n + 1)

for _ in range(m):
    u, v  = integers()
    deg[u] += 1
    deg[v] += 1

deg1 = deg.count(1)
deg2 = deg.count(2)
degN = deg.count(n - 1)

if m == n - 1 and deg1 == 2 and deg2 == n - 2:
    print("bus topology")
elif m == n and deg2 == n:
    print("ring topology")
elif m == n - 1 and deg1 == n - 1 and degN == 1:
    print("star topology")
else:
    print("unknown topology")