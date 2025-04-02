# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        def checker(mid):
            count = 0
            for candy in candies:
                if candy >= mid:
                    count += candy // mid
            if count >= k:
                return True
            else:
                return False
        l = 1
        h = max(candies)

        while l <= h:
            mid =( l + h) // 2
            if checker(mid):
                l = mid + 1
            else:
                h = mid - 1
        return h
        