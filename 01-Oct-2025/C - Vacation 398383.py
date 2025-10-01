# Problem: C - Vacation - https://atcoder.jp/contests/dp/tasks/dp_c

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

n = integer()

nums = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[0] * 3 for _ in range(n + 1)]

#base case
dp[1][0], dp[1][1], dp[1][2] = nums[0]

for i in range(2,n + 1):
    a,b,c = nums[i - 1]
    dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + a
    dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + b
    dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + c

print(max(dp[n]))