# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}
        def dp(i,hasStock):
            if i == len(prices):
                if hasStock:
                    return float('-inf')
                else:
                    return 0 
                    
            if (i,hasStock) in memo:
                return memo[(i,hasStock)]
            ans = 0
            if hasStock:
                sell = dp(i + 1,False) + prices[i] - fee
                skip = dp(i + 1, True)
                ans = max(sell,skip)
            else:
                buy = dp(i + 1, True) - prices[i]
                skip = dp(i + 1, False)
                ans = max(buy,skip)
            memo[(i,hasStock)] = ans
            return ans
        return dp(0,False)
            
