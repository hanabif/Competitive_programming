# Problem: Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

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

n , m, k = integers()
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

for _ in range(m):
    u , v = integers()

query = []
for _ in range(k):
    query.append(stringList())
query = query[::-1]

ans = []
for i in range(k):
    if query[i][0] == "ask":
        if find(int(query[i][1])) == find(int(query[i][2])):
            ans.append('YES')
        else:
            ans.append('NO')
    else:
        union(int(query[i][1]),int(query[i][2]))

ans = ans[::-1]
for a in ans:
    print(a)


        

