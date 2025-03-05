# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

#© @haymi

import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter
 
def string(): return sys.stdin.readline().strip()
def integer(): return int(sys.stdin.readline().strip())
def integers(): return map(int, sys.stdin.readline().strip().split())
def List(): return list(map(int, sys.stdin.readline().strip().split()))
def strings(): return map(str, sys.stdin.readline().strip().split())
def stringList(): return list(map(str, sys.stdin.readline().strip().split()))
def Matrix(n): return list(list(map(int, sys.stdin.readline().strip().split())) for i in range(n))

n = integer()
cost = List()



prefix = [0] * (n + 1)

for i in range(n):
    prefix[i + 1] = prefix[i] + cost[i]

sorted_cost = sorted(cost)
sorted_prefix = [0] * (n + 1)

for i in range(n):
    sorted_prefix[i + 1] = sorted_prefix[i] + sorted_cost[i]

m = integer()
while m:
    m-=1
    Type, l, r = integers()
    
    if Type == 1:  
       print(prefix[r] - prefix[l - 1])
    else:
        print(sorted_prefix[r] - sorted_prefix[l - 1])