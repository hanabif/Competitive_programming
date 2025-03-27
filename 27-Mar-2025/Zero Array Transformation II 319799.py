# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def checker(num):
            nonlocal queries
            diff = [0] * (len(nums) + 1)
            
            for i in range(num):
                diff[queries[i][0]] -= queries[i][2]
                diff[queries[i][1] + 1] += queries[i][2]
                
            pref = [0] * (len(diff))
            acc = 0
            for i in range(len(diff)):
                acc += diff[i]
                pref[i] = acc

            for i in range(len(nums)):
                if nums[i] > abs(pref[i]):
                    return False
              
            return True
            
   
        l = 0
        r = len(queries)
        while l <= r:
            mid = (l + r) // 2
            if checker(mid):
                r = mid - 1
            else:
                l = mid + 1
        if l > len(queries):
            return -1
        else:
            return l 

        
