# Problem: 3 Sum Closest - https://leetcode.com/problems/3sum-closest/description/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float (-inf)
       

        for i in range(len(nums)):
            right = len(nums) - 1
            left = i + 1
            while left < right:
                summ = nums[i] + nums[right] + nums[left]

                if abs(target - summ) < abs(target - closest):
                    closest = summ
                if summ > target:
                    right-=1
                elif summ < target:
                    left+=1
                else:
                    return summ
        return closest

            

        