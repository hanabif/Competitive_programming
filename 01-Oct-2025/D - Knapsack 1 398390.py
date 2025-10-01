# Problem: D - Knapsack 1 - https://atcoder.jp/contests/dp/tasks/dp_d

from functools import reduce
import sys
from math import ceil, floor, gcd, log2
from collections import defaultdict, Counter,deque
from bisect import bisect_left,bisect_right
from itertools import accumulate
from functools import lru_cache

def string(): return sys.stdin.readline().strip()
def integer(): return int(sys.stdin.readline().strip())
def integers(): return map(int, sys.stdin.readline().strip().split())
def List(): return list(map(int, sys.stdin.readline().strip().split()))
def strings(): return map(str, sys.stdin.readline().strip().split())
def stringList(): return list(map(str, sys.stdin.readline().strip().split()))
def Matrix(n): return list(list(map(int, sys.stdin.readline().strip().split())))

N,W = integers()
weights = []
values = []
for _ in range(N):
    wi, vi = map(int, input().split())
    weights.append(wi)
    values.append(vi)

dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(N - 1, -1,-1):
    for rem in range(W + 1):
        skip = dp[i + 1][rem]
        take = 0
        if rem >= weights[i]:
            take = dp[i + 1][rem - weights[i]] + values[i]
        dp[i][rem] = max(take, skip)

ans = dp[0][W]
print(ans)
