# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        countMap= Counter(answers)
        mini=0
        for key, count in countMap.items():
            groups=math.ceil(count/(key+1))
            mini+=groups*(key+1)
        return mini
        