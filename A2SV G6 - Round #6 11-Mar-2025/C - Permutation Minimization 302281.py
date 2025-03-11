# Problem: C - Permutation Minimization - https://codeforces.com/gym/594077/problem/C

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

t = integer()
while t:
    t-=1
    n = integer()
    nums = List()

    deq =deque([nums[0]])
    
    for i in range(1,n):
        if nums[i] < deq[0]:
            deq.appendleft(nums[i])
        else:
            deq.append(nums[i])
    print(" ".join(list(map(str,deq))))