# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xor = [arr[0]]
        for i in range(1, len(arr)):
            xor.append(xor[i-1] ^ arr[i])

        ans = []
        for u,v in queries:
            if u:
                ans.append(xor[v] ^ xor[u - 1])
            else:
                ans.append(xor[v])
        return ans