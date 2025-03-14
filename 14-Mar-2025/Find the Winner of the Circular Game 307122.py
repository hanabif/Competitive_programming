# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1, n + 1))  
        def win(i):
            if len(friends) == 1:
                return friends[0]
            i = (i + k - 1) % len(friends)
            friends.pop(i)
            return win(i)
        return win(0)
        



