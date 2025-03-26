# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def checker(num):
            nonlocal cars
            car = 0
            for i in range(len(ranks)):
                car += int(sqrt(num // ranks[i])) 
            if car >= cars:
                return True
            return False
        
        l = 1
        r = min(ranks)*(cars**2)
       
        while l < r:
            mid = (l + r )// 2
            if checker(mid):
                r = mid 
            else:
                l = mid + 1
        return l
        
        