# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gdc(a,b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        count = 0
        for i in range(len(nums)):
            curr_gcd = 0
            for j in range(i,len(nums)):
                curr_gcd = gcd(curr_gcd , nums[j])
                if curr_gcd == k:
                    count += 1
                elif curr_gcd < k:
                    break
        return count
