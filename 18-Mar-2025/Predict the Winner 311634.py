# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        score = 0
        def win(l , r):
            if l == r:
                return nums[l]
            score = max(nums[l] - win(l + 1, r), nums[r] - win(l , r - 1))
            return score
        res = 0
        res = win(0 , len(nums) - 1)
        if res >= 0:
            return True
        else:
            return False
        