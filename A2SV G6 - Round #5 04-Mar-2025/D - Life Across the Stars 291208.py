# Problem: D - Life Across the Stars - https://codeforces.com/gym/591928/problem/D

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

n = integer()
people = []
while n:
    n-=1
    people.append(tuple(list(integers())))

events = defaultdict(int)
for b, d in people:
    events[b]+=1
    events[d]-=1

sorted_years = sorted(events.keys())


max_alive = 0
current_alive = 0
max_year = None

for year in sorted_years:
    current_alive+= events[year]
    
    if current_alive > max_alive:
        max_alive = current_alive
        max_year = year
    
print(max_year , max_alive)



