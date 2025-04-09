# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        sorted_vals = inorder(root)
        
        def buildBST(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(sorted_vals[mid])
            node.left = buildBST(left, mid - 1)
            node.right = buildBST(mid + 1, right)
            return node
        return buildBST(0, len(sorted_vals) - 1)
        