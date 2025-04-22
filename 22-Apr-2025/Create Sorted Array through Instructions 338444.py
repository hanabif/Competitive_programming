# Problem: Create Sorted Array through Instructions - https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        sorted_list = []
        cost = 0

        for x in instructions:
            pos = bisect_left(sorted_list, x)
            greater = len(sorted_list) - bisect_right(sorted_list, x)
            cost = (cost + min(pos, greater)) % MOD 
            if cost < 0:
                cost += MOD  
            sorted_list.insert(pos, x) 

        return cost
        