# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left=0
        right = len(skill)-1
        sums=set()
        pairs=[]
        ans=0
        while left<len(skill) and left<right:
            sums.add(skill[left]+skill[right])
            pairs.append((skill[left],skill[right]))
            left+=1
            right-=1
        if len(sums)==1:
            for i,j in pairs:
                ans+=i*j
        else:
            ans=-1
        return ans

                




        