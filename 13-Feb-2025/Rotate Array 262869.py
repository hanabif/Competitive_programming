# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reversing(left,right):
            while left<right:
                nums[left] , nums[right]= nums[right], nums[left]
                left+=1
                right-=1
        
        k = k % len(nums)
        reversing(0, len(nums)-1)
        reversing(0,k-1)
        reversing(k, len(nums)-1)
        

        