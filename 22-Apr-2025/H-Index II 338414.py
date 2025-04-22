# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l = 0
        h = n

        while l < h:
            mid = (l + h) // 2
            if citations[mid] >= n - mid:
                h = mid
            else:
                l = mid + 1
        
        return n - l