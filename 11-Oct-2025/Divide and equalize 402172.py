# Problem: Divide and equalize - https://codeforces.com/problemset/problem/1881/D

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

def factorize(n: int) -> list[int]:
    factorization: list[int] = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factorization.append(d)
            n //= d
        d += 1
    if n > 1:
        factorization.append(n)

    return factorization

t = integer()
for _ in range(t):
    n = integer()
    nums = List()

    factors = defaultdict(int)
    for num in nums:
        fac = factorize(num)
        for f in fac:
            factors[f] += 1
    
    
    ans = 'YES'
    for f in factors.values():
        if f % n != 0:
            ans = 'NO'
            break
        
    print(ans)