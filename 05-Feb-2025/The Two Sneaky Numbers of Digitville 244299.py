# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans=[]
        Hash=defaultdict(int)
        for i in nums:
            Hash[i]+=1
        for key,value in Hash.items():
            if value==2:
                ans.append(key)
        return ans
        