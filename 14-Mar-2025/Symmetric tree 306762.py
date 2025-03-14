# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def sym(l , r):
            if not l and not r:
                return True
            if not l and r:
                return False
            if not r and l:
                return False
            
            val = l.val == r.val
            ans1 = sym(l.left , r.right)
            ans2 = sym(l.right , r.left)

            return ans1 and ans2 and val
        return sym(root.left, root.right)

        