# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        Hash=Counter(nums)
        ans=[]
        evens,leftovers=0,0
        for value in Hash.values():
            evens+=value//2
            leftovers+=value%2
        return [evens,leftovers]


        