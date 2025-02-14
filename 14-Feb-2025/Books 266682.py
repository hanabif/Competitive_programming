# Problem: Books - https://codeforces.com/contest/279/problem/B

#© @Haymi

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

n , t = integers()
nums = List()

book_sum = 0
counter = 0
left = 0
ans = 0
for right in range(n):
    book_sum+=nums[right]
    
    while book_sum > t:
       
        book_sum-= nums[left]
        left+=1
    ans = max( ans, right - left +1)
print(ans)   
