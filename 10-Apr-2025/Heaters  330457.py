# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        res = float("-inf")
        houses.sort()
        heaters.sort()
        for h in houses:
            idx = bisect_left(heaters,h)

            right_dist = heaters[idx] - h if idx < len(heaters) else float('inf')
            left_dist = h - heaters[idx - 1] if idx > 0 else float('inf')
            
            ans = min(left_dist, right_dist)
            res = max(res, ans)
        return res
