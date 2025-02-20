# Problem: B - Anansi and Trip-Photographs - https://codeforces.com/gym/588468/problem/B

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

t= integer()
while t:
    t-=1
    n , x = integers()
    row = List()
    
    row.sort() 
    left = n - 1 
    right = 2 * n - 1  
    possible = True
    while left >= 0:
        if row[right] - row[left] < x:
            print("NO")
            possible = False
            break
        right -= 1
        left -= 1
    if possible:
        print("YES")
        







    
        

    

        
    
            
    
        
        

    
        