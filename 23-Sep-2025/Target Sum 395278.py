# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {} 
        def dp(i,curr_sum):
            if i == len(nums):
                if curr_sum == target:
                    return 1
                else:
                    return 0

            if (i,curr_sum) in memo:
                return memo[(i,curr_sum)]
            
            memo[(i,curr_sum)] = dp(i + 1, curr_sum + nums[i]) +  dp(i + 1, curr_sum - nums[i])
            return memo[(i,curr_sum)]
        
        return dp(0,0)
            