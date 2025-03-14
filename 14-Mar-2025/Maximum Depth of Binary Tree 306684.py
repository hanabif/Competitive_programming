# Problem: Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxi = 0
        def depth(root, count):
            nonlocal maxi
            if not root:
                return 0
            
            if root.left:
                depth(root.left,count + 1)
            if root.right:
                depth(root.right, count + 1)
            maxi = max(maxi, count)

        depth(root, 1)
        return maxi
             
            
        