# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)

        if target % 2 != 0:
            return False

        memo = {}
        def dp(i,target):
            if i >= len(nums) or target <= 0:
                return target == 0
        
            if (i,target) in memo:
                return memo[(i,target)] 
                
            memo[(i,target)] = dp(i + 1, target) or dp(i + 1, target - nums[i])
            return memo[(i,target)]
        return dp(0,target // 2)