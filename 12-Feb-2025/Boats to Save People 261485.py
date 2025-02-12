# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left=0
        right = len(people)-1
        ans=0
        while left<=right:
            remaining=limit-people[right]
            right-=1
            ans+=1
            if left<=right and remaining>=people[left]:
                left+=1
        return ans

           
        
        




        