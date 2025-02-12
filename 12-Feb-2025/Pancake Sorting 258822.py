# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        right = len(arr) - 1
        ans = []
        while right>0:
            max_index=arr.index(max(arr[:right+1]))
            if max_index!=right:
                if max_index!=0:
                    arr[:max_index+1]=arr[:max_index+1][::-1]
                    ans.append(max_index+1)
                
                arr[:right+1]=arr[:right+1][::-1]
                ans.append(right+1)
            right -= 1
        return ans