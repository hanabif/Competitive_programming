# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curSum = 0
        def dfs(node):
            nonlocal curSum
            if not node:
                return 
            
            dfs(node.right)
            temp = node.val
            node.val += curSum
            curSum += temp
            dfs(node.left)
        dfs(root)
        return root
        