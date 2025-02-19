# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

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
A = List()
m = integer()
B = List()

pre_A = [0] * (n + 1)
for i in range(1, n+1):
    pre_A[i] = pre_A[i - 1] + A[i - 1]
 
pre_B = [0] * (m + 1)
for i in range(1, m+1):
    pre_B[i] = pre_B[i - 1] + B[i - 1]

i, j = 0, 0  
count = 0  

while i < n and j < m:
    sum1 = pre_A[i+1]
    sum2 = pre_B[j+1]

    if sum1 == sum2:
        count+=1
        i+=1
        j+=1
    elif sum1<sum2:
        i+=1
    else:
        j+=1
if i == n and j ==m:
    print(count)
else:
    print(-1)
        

