# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, row: int) -> List[int]:
        if row == 0:
            return [1]
        if row == 1:
            return [1,1]
        
        arr = self.getRow(row - 1)
        ans = [1]
        for i in range(1,len(arr)):
            ans.append(arr[i] + arr[i - 1])
        ans.append(1)
        return ans
        