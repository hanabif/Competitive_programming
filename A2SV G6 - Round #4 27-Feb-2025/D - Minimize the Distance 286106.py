# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

import sys


    
n = int(sys.stdin.readline().strip())
points = list(map(int, sys.stdin.readline().split()))
points.sort()
if n % 2 == 1:
    print (points[n // 2])
else:
    print (points[(n // 2) - 1])
