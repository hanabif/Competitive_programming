# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        for i in range(1,n + 1):
            bits = []
            while i != 0:
                rem = i % 2
                i = i // 2
                bits.append(rem)
            ones = bits.count(1)
            ans.append(ones)
        return ans

        