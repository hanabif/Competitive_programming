# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = [0] * k
        for n in arr:
            freq[n % k] += 1  
        if k % 2 == 0 and (freq[k // 2] % 2 == 1 or freq[0] % 2 == 1):
            return False
        for i in range(1, k):
            if freq[i] != freq[(-i) % k]:
                return False
        return True
        