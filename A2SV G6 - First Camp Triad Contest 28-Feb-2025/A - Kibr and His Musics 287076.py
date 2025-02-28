# Problem: A - Kibr and His Musics - https://codeforces.com/gym/589822/problem/A

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

n,m = integers()
playlist = [0]
for _ in range(n):
    duration = List()
    playlist.append(duration[0]*duration[1] + playlist[-1])

moments = List()
    
i = 1
for moment in moments:
    while  i < len(playlist) and playlist[i] < moment :
        i+=1
    print(i)
