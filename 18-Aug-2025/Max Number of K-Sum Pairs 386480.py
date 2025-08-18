# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        i = 0
        j = len(nums) - 1
        nums.sort()

        count = 0
        while i < j:
            if nums[i] + nums[j] < k:
                i += 1
            elif nums[i] + nums[j] > k:
                j -= 1
            else:
                i += 1
                j -= 1
                count += 1
        return count
        