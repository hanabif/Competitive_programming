# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

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

decr = deque()
incr = deque()
ans = 0
left = 0
for right in range(n):
    while decr and decr[-1] < nums[right]:
        decr.pop()
    decr.append(nums[right])

    while incr and incr[-1] > nums[right]:
        incr.pop()
    incr.append(nums[right])


    while decr[0] - incr[0] > k:
        if decr[0] == nums[left]:
            decr.popleft()
        if incr[0] == nums[left]:
            incr.popleft()
        left +=1
    ans += right - left + 1
print(ans) 
