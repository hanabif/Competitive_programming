# Problem: D - Creating an a-Good String - https://codeforces.com/gym/596141/problem/D

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
    n = integer()
    s = string()

    def count(start,end,char, s):
        count = 0
        for i in range(start,end):
            if s[i] != char:
                count+=1
        return count
    

    def can(i,j,ch, s):
        if i == j:
            return 0 if s[i] == ch else 1
        
        mid = (i + j )// 2
        left = count(i,mid + 1,ch , s)
        right = count(mid + 1, j + 1 , ch, s)
        
        left_res = can(i , mid,chr(ord(ch) + 1) , s)
        right_res = can(mid + 1, j , chr(ord(ch) + 1), s)
        return min(left + right_res , right + left_res)
    
    ans = 0
    ans = can(0 , n - 1, 'a', s)
    print(ans)
    



        


    
