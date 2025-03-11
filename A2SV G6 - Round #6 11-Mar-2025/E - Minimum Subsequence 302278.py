# Problem: E - Minimum Subsequence - https://codeforces.com/gym/594077/problem/E

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
    nums = list(map(int,input()))
    
    count = 0
    zeros = []
    ones = []
    res = [0] * n
    for i, num in enumerate(nums):
        if num == 0:
            if ones:
                index = ones.pop()
            else:
                count+=1
                index = count
            zeros.append(index)
        else:
            if zeros:
                index = zeros.pop()
            else:
                count +=1
                index = count
            ones.append(index)
        
        res[i] = index
    print(count)
    print(*res)