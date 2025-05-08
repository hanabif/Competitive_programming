# Problem: Experience - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/C

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
point = [0 for _ in range(n + 1)]

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return parent[x]


def union(a,b):
    parA = find(a)
    parB = find(b)
    if parA != parB:
        if size[parA] > size[parB]:
            parent[parB] = parent[parA]
            size[parA] += size[parB]
            point[parB] -= point[parA]
        else:
            parent[parA] = parent[parB]
            size[parB] += size[parA]
            point[parA] -= point[parB]

def add(num):
    total = 0
    while num != parent[num]:
        total += point[num]
        num = parent[num]
    
    return total + point[num]

ans = []
for _ in range(m):
    query = stringList()
    if query[0] == 'add':
        par = find(int(query[1]))
        point[par] += int(query[2])
    elif query[0] == 'join':
        union(int(query[1]),int(query[2]))
    else:
        ans.append(add(int(query[1])))

for char in ans:
    print(char)
