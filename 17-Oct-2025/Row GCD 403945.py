# Problem: Row GCD - https://codeforces.com/problemset/problem/1458/a

from functools import reduce
import sys
from math import ceil, floor, gcd, log2
from collections import defaultdict, Counter,deque
from bisect import bisect_left,bisect_right
from itertools import accumulate
from functools import lru_cache
import math

def string(): return sys.stdin.readline().strip()
def integer(): return int(sys.stdin.readline().strip())
def integers(): return map(int, sys.stdin.readline().strip().split())
def List(): return list(map(int, sys.stdin.readline().strip().split()))
def strings(): return map(str, sys.stdin.readline().strip().split())
def stringList(): return list(map(str, sys.stdin.readline().strip().split()))
def Matrix(n): return list(list(map(int, sys.stdin.readline().strip().split())))

n,m = integers()
a = List()
b = List()

base = 0
for i in range(1,n):
    base = math.gcd(base,a[i] - a[0])

for j in b:
    print(math.gcd(base, a[0] + j), end=' ')
