# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

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

n , k =integers()

nums = List()
arr = []
for i in range(1,n):
    arr.append(nums[i] - nums[i - 1])
arr.sort()
summ = 0
for j in range(n-k):
    summ += arr[j]
print(summ)