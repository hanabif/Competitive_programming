# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(root,val):
            if not root:
                return TreeNode(val)
            if root.val > val:
                if root.left:
                    insert(root.left, val)
                else:
                    new = TreeNode(val)
                    root.left = new
            if root.val < val:
                if root.right:
                    insert(root.right, val)
                else:
                    new = TreeNode(val)
                    root.right = new
            return root
        return insert(root,val)
          
            


        