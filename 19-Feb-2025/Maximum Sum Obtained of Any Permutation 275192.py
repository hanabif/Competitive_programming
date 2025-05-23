# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)     
            
        freq = [0] * n
        for start, end in requests:
            freq[start] += 1
            if end + 1 < n:
                freq[end + 1] -= 1
        
        for i in range(1, n):
            freq[i] += freq[i - 1]
        
        freq.sort(reverse=True)
        nums.sort(reverse=True)
        
        total_sum = 0
        for i in range(n):
            total_sum += freq[i] * nums[i]
            total_sum %= MOD
        
        return total_sum
            