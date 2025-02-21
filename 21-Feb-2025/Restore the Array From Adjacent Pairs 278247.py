# Problem: Restore the Array From Adjacent Pairs - https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/description/

class Solution:
    def restoreArray(self, adj: List[List[int]]) -> List[int]:
        freq = defaultdict(int)
        for p1 , p2 in adj:
            freq[p1]+=1
            freq[p2]+=1
        
        ans = []
        start = 0
        for num,f in freq.items():
            if f==1:
                start = num
                break
        
        graph=defaultdict(list)
        for p1,p2 in adj:
            graph[p1].append(p2)
            graph[p2].append(p1)

        visited=set()
        def dfs(start):
            ans.append(start)
            visited.add(start)
            for nbr in graph[start]:
                if nbr not in visited:
                    dfs(nbr)
        dfs(start)
        return ans
        


        