# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        running = 0
        count[0]=1
        ans = 0
        for  i in range(len(nums)):
            running+= nums[i]
            remainder = running % k
            ans += count[remainder]
            count[remainder]+=1
        return ans
        