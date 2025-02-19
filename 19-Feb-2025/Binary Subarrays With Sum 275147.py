# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = defaultdict(int)
        running = 0
        count[0]=1
        ans = 0
        for  i in range(len(nums)):
            running+= nums[i]
            target = running - goal
            ans += count[target]
            count[running]+=1
        return ans
        