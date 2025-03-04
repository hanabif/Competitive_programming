# Problem: C - Escape-Proof Transfers - https://codeforces.com/gym/591928/problem/C

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

n , t , c = integers()
nums = List()

valid, count= 0, 0
for i in range(c):
    if nums[i] <= t:
        count+=1

if count == c:
    valid+=1

for i in range(c,n):
    if nums[i - c] <= t:
        count-=1
    if nums[i] <= t:
        count+=1
    
    if count == c:
        valid +=1
print(valid)

    
    
