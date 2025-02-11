# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        left=0
        right=len(piles)-1
        count=0
        while left<right:
            count+=piles[right-1]
            left+=1
            right-=2
        return count

            

        