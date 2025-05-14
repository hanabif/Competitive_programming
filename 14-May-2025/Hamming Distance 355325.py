# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num = x ^ y
       
        cnt = 0
        for i in range(32):
            index = 1 << i

            if index & num != 0: 
                cnt += 1

        return cnt

      