# Problem: B - Fix the Forecast! - https://codeforces.com/gym/591928/problem/B

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
    n ,k =integers()
    a = List()
    b = List()
    mapping = sorted(enumerate(a), key=lambda x: x[1])
    new_b = sorted(b)

    ans = [0]*n
    i = 0

    for index , num in mapping:
        while i < n and new_b[i] < num - k:
            i+=1
        
        ans[index]= new_b[i]
        i+=1
    print(" ".join(map(str,ans)))
    
   