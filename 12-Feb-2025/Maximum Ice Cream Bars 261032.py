# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        maxim=max(costs)
        new=[0]*(maxim+1)
        for cost in costs:
            new[cost]+=1
        target=0
        for index,num in enumerate(new):
            for i in range(num):
                costs[target]=index
                target+=1
        print(costs)
        cost=0
        ans=0
        for j in range(len(costs)):
            if costs[j]+cost<=coins:
                cost+=costs[j]
                ans=j+1
            else:
                break
        return ans
