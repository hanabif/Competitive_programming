# Problem: C - Minimal TV Subscriptions - https://codeforces.com/gym/588468/problem/C

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
    n , k ,d = integers()
    shows = List()
    show_count = defaultdict(int)
    unique = 0
    min_unique = float('inf')

    for i in range(d):
        if show_count[shows[i]] == 0:
            unique += 1  
        show_count[shows[i]] += 1
    min_unique = min(unique, min_unique)

    for i in range(d,n):
        left = shows[i-d]
        show_count[left]-=1
        if show_count[left] == 0:
            unique-=1
        
        right = shows[i]
        if show_count[right] == 0:
            unique+=1
        show_count[right]+=1
        
        min_unique = min(min_unique , unique)
    print(min_unique)
