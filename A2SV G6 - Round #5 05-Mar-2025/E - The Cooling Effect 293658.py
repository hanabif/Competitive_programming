# Problem: E - The Cooling Effect - https://codeforces.com/gym/591928/problem/E

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
    sys.stdin.readline()
    n , k =integers()
    positions = List()
    temperatures = List()

    temp = [float("inf")] * n
    for i in range(k):
        temp[positions[i] - 1] = temperatures[i]
    
    for i in range(1,n):
        temp[i] = min(temp[i - 1] + 1, temp[i])
    for i in range(n - 2,-1, -1):
        temp[i] = min(temp[i + 1] + 1, temp[i])
    print(" ".join(map(str,temp)))