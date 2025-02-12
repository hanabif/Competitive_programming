# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:  
        people = defaultdict(int)
        for i in range(len(names)):
            people[heights[i]] = names[i]
        
        heights.sort(reverse=True)
        result = []
        for height in heights:
            result.append(people[height])
        
        return result
