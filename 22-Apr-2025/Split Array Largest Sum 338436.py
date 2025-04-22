# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def checker(mid):
            subarray = 0
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > mid:
                    subarray += 1
                    curSum = n
            if subarray + 1 <= k:
                return True
            return False
        
        l = max(nums)
        h = sum(nums)
        while l <= h:
            mid = (l + h) // 2
            if checker(mid):
                ans = mid
                h = mid - 1
            else:
                l = mid + 1
        return ans



        