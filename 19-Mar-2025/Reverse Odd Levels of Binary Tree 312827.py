# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return []
        
        que = deque([root])
        level = 0

        while que:
            if level % 2 != 0:
                l , r = 0 , len(que) - 1
                while l<r:
                    que[l].val , que[r].val = que[r].val , que[l].val
                    l += 1
                    r -= 1

            for _ in range(len(que)):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            level += 1
        return root


        