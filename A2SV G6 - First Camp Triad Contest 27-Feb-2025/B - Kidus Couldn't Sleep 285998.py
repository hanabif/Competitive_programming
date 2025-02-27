# Problem: B - Kidus Couldn't Sleep - https://codeforces.com/gym/589822/problem/B

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

n , k = integers()
arr = List()
window = sum(arr[:k])
total = window

for right in range(k , n):
    window+=arr[right] - arr[right-k]
    total+=window
   
print(f"{total/(n-k+1):.10f}")