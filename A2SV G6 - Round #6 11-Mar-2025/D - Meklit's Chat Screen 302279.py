# Problem: D - Meklit's Chat Screen - https://codeforces.com/gym/594077/problem/D

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


n , k = integers()

nums = List()
deq = deque()
active = set()

for i in range(n):
    if nums[i] in active:
        continue
    if len(deq) == k or (deq and deq[0] == nums[i]):
        temp = deq.pop()
        active.remove(temp)
    deq.appendleft(nums[i])
    active.add(nums[i])

print(len(deq))
print(*deq)