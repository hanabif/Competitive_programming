# Problem: B - Frog 2 - https://atcoder.jp/contests/dp/tasks/dp_b

from functools import reduce
import sys
from math import ceil, floor, gcd, log2
from collections import defaultdict, Counter,deque
from bisect import bisect_left,bisect_right
from itertools import accumulate

def string(): return sys.stdin.readline().strip()
def integer(): return int(sys.stdin.readline().strip())
def integers(): return map(int, sys.stdin.readline().strip().split())
def List(): return list(map(int, sys.stdin.readline().strip().split()))
def strings(): return map(str, sys.stdin.readline().strip().split())
def stringList(): return list(map(str, sys.stdin.readline().strip().split()))
def Matrix(n): return list(list(map(int, sys.stdin.readline().strip().split())))

n,k = integers()
nums = List()
memo = {}

from types import GeneratorType

def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

@bootstrap
def dp(i):
    if i == 0:
        yield 0
    if i == 1:
        memo[1] = abs(nums[1] - nums[0])
        yield memo[1]
    if i not in memo:
        mini = float("inf")
        for j in range(1,k + 1):
            if i - j >= 0: 
                dp1 = yield dp(i- j)
                mini = min(mini, abs(nums[i] - nums[i - j]) + dp1)
            memo[i] = mini
    yield memo[i]
print(dp(n - 1))