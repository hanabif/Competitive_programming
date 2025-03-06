# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

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

t = integer()
while t:
    t-=1
    n = integer()
    red = List()
    m = integer()
    blue = List()

    pre_red = [0] * (n + 1)
    for i in range(n):
        pre_red[i + 1] = red[i] + pre_red[i]
    
    pre_blue = [0] * (m + 1)
    for j in range(m):
        pre_blue[j + 1] = blue[j] + pre_blue[j]
    
    ans = max(pre_blue) + max(pre_red)
    print(ans)
