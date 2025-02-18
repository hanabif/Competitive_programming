# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, pt: List[int], tasks: List[int]) -> int:
        left = 0
        core = 0
        max_sum = 0
        pt.sort()
        tasks.sort(reverse= True)
        for i in range(len(tasks)):
            max_sum = max(max_sum , tasks[i] + pt[left])
            core+=1
            if core%4 == 0:
                left+=1
        return max_sum

        