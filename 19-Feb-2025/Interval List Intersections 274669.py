# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, first: List[List[int]], second: List[List[int]]) -> List[List[int]]: 
        i = 0
        j = 0
        ans=[]

        while i < len(first) and j < len(second):
            lesser = max(first[i][0] , second[j][0])
            higher = min(first[i][1] , second[j][1])

            if lesser <= higher:
                ans.append([lesser , higher])
            
            if first[i][1] < second[j][1]:
                i+=1
            else:
                j+=1
        return ans