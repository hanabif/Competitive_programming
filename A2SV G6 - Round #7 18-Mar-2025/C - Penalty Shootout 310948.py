# Problem: C - Penalty Shootout - https://codeforces.com/gym/596141/problem/C

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
    shoot = list(map(str,string()))
    index1 = 0
    index2 = 0

    team1 = 0
    team2 = 0

    rem1 = 5
    rem2 = 5
    for i in range(len(shoot)):
        if i % 2 == 0:
            if shoot[i] == '1' or shoot[i] == '?':
                team1 += 1 
            rem1 -=1
        else:
            if shoot[i] == '1':
                team2 += 1
            rem2 -=1
        if team1 > team2 + rem2:
            index1 = i + 1
            break
    else:
        index1 = 10

    team1 = 0
    team2 = 0   
    rem1 = 5
    rem2 = 5
    for i in range(len(shoot)):
        if i % 2 == 0:
            if shoot[i] == '1' :
                team1 += 1 
            rem1 -=1
        else:
            if shoot[i] == '1' or shoot[i] == '?':
                team2 += 1
            rem2 -=1
        if team2 > team1 + rem1:
            index2 = i + 1
            break
    else:
        index2 = 10
    print(min(index1 , index2))



