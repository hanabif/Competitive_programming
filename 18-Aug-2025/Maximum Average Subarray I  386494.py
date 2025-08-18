# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum= sum(nums[:k])
        maxSum=cur_sum
        for i in range(k, len(nums)):
            cur_sum = cur_sum + nums[i] - nums[i-k]
            maxSum= max(maxSum , cur_sum)
        return maxSum/k


        