# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def diff(node, mini, maxi):
            if not node:
                return maxi - mini
            
            mini = min(mini,node.val)
            maxi = max(maxi, node.val)

            left_diff = diff(node.left, mini, maxi)
            right_diff = diff(node.right , mini , maxi)

            return max(left_diff, right_diff)
        return diff(root, root.val, root.val)
        