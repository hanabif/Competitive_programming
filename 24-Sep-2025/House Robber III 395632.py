# Problem: House Robber III - https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def dp(node):
            if not node:
                return 0
            if node in memo:
                return memo[node]
            take = node.val
            if node.right and node.left:
                take = dp(node.left.left) + dp(node.left.right) + dp(node.right.left) + dp(node.right.right) + node.val
            elif node.left:
                take = dp(node.left.left) + dp(node.left.right) + node.val
            elif node.right:
                take = dp(node.right.left) + dp(node.right.right) + node.val
            
            skip = dp(node.left) + dp(node.right)
            memo[node] = max(skip, take)
            return memo[node]
        return dp(root)
