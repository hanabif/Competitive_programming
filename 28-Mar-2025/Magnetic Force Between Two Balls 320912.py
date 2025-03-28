# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, pos: List[int], m: int) -> int:
        pos.sort()
        def checker(force):
            count = 1
            temp = pos[0]
            for i in range(1, len(pos)):
                if pos[i] - temp >= force:
                    temp = pos[i]
                    count += 1
                if count >= m:
                    return True

            return False

        l = 0
        r = max(pos)
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            if checker(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans 
        