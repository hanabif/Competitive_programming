# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        que = deque([root] if root else [])
        isReverse = False
        while que:
            level = []
            for i in range(len(que)):
                node = que.popleft()
                level.append(node.val)

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            if isReverse:
                level.reverse()
            res.append(level)
            isReverse = not isReverse
        return res


        