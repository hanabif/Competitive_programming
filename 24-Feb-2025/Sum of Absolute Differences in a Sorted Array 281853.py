# Problem: Sum of Absolute Differences in a Sorted Array - https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        left_sum = 0
        ans = []

        for i , n in enumerate(nums):
            right_sum = total - n - left_sum
            left_size , right_size = i , len(nums) - i - 1

            ans.append(
                left_size * n - left_sum + right_sum - right_size * n
            )
            left_sum+=n
        return ans
        