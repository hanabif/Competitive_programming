# Problem: Spanning Tree - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/E

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

n,m = integers()

parent = [i for i in range(n + 1)]
size = [1 for _ in range(n + 1)]


def find(x):
    if parent[x] == x:
        return parent[x]
    parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    parA = find(a)
    parB = find(b)
    if parA != parB:
        if size[parA] > size[parB]:
            parent[parB] = parent[parA]
            size[parA] += size[parB]
        else:
            parent[parA] = parent[parB]
            size[parB] += size[parA]

edges = []
for _ in range(m):
    nums = List()
    edges.append((nums[2], nums[0],nums[1]))

total = 0
edges.sort()
for w, u ,v in edges:
    if find(u) == find(v):
        continue 
    union(u,v)
    total +=w

print(total)



