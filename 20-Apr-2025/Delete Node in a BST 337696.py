# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def get_min_node(curr):
            while curr.left:
                curr = curr.left
            return curr

        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
           
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                
                successor = get_min_node(root.right)
                root.val = successor.val
                root.right = self.deleteNode(root.right, successor.val)
        
        return root
        
        