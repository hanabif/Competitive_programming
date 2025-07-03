# Problem: Skibidus and Fanum Tax (hard version) - http://codeforces.com/problemset/problem/2065/C2

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

n = integer()
tree = [[] for _ in range(n + 1)]
for i in range(2, n + 1):
    parent = integer()
    tree[parent].append(i)

is_spruce = True
for i in range(1,n + 1):
    children = tree[i]
    if children:
        count = 0
        for child in children:
            if not tree[child]:
                count += 1
        if count < 3:
            is_spruce = False
            break

if is_spruce:
    print("Yes")
else:
    print("No")
