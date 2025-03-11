# Problem: B - Nafargi's Binary Reduction Game - https://codeforces.com/gym/594077/problem/B

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

nums = list(map(int,input()))

if not nums:
    print("0")
ones = nums.count(1)
zeros = nums.count(0)
print(abs(ones - zeros))