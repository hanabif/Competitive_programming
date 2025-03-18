# Problem: A - Free Ice Cream for the Kids - https://codeforces.com/gym/596141/problem/A

#© @haymi

import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
 
def string(): return sys.stdin.readline().strip()
def integer(): return int(sys.stdin.readline().strip())
def integers(): return map(int, sys.stdin.readline().strip().split())
def List(): return list(map(int, sys.stdin.readline().strip().split()))
def strings(): return map(str, sys.stdin.readline().strip().split())
def stringList(): return list(map(str, sys.stdin.readline().strip().split()))
def Matrix(n): return list(list(map(int, sys.stdin.readline().strip().split())) for i in range(n))

n , x = integers()
nums = []
count = 0
for _ in range(n):
    nums.append(tuple(stringList()))

for s,num in nums:
    num = int(num)
    if s == '+':
        x += num
    else:
        if x < num:
            count +=1
        else:
            x -= num
print(x,count)

