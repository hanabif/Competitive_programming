# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        running = 0
        count[0]=1
        ans = 0
        for  i in range(len(nums)):
            running+= nums[i]
            target = running - k
            ans += count[target]
            count[running]+=1
        return ans

        
