# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        length = 2**n - 1

        def bit(length, k):
            if length == 1:
                return "0"

            half = length // 2
            if k <= half:
                return bit(half, k)
            elif k > half + 1:
                res = bit(half, 1 + length - k)
                return "0" if res == "1" else "1"
            else:
                return "1"

        return bit(length, k)
