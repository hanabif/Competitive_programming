# Problem: Reveal Cards In Increasing Order - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        que = deque()
        reveal = []
        ans = [0] * len(deck)

        for i in range(len(deck)):
            que.append(i)
        for j in range(len(deck)):
            reveal.append(que.popleft())
            if que:
                que.append(que.popleft())
        deck.sort()
        for i in range(len(deck)) :
            ans[reveal[i]] = deck[i]
        return ans