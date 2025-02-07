# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        Hash=defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                Hash[nums[i]*nums[j]]+=1
        arithmetic_sum,res, perm=0,0,0
        for value in Hash.values():
            arithmetic_sum= (value*(value-1))//2
            perm+=arithmetic_sum*8

        return perm


   