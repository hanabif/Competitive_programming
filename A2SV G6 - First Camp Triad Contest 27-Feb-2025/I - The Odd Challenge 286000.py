# Problem: I - The Odd Challenge - https://codeforces.com/gym/589822/problem/I

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

t = integer()
while t:
    t-=1
    size , q = integers()
    arr = List()
    
    arr_sum = sum(arr)
    prefix_sum = [0] * (size + 1)
   
    for i in range(1, size + 1):
        prefix_sum[i] = arr[i-1] + prefix_sum[i-1]
    
    for _ in range(q):
        l , r ,k = integers()
        diff = prefix_sum[r] -  prefix_sum[l - 1] 
        before = arr_sum - diff
        total = before + ((r - l + 1)* k)
        
        if total%2!= 0:
            print("YES")
        else:
            print("NO")
        

        
        

