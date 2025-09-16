# Problem: Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        que = deque([root])
        
        while que:
            rightSide = None
            qLen = len(que)

            for i in range(qLen):
                node = que.popleft()
                if node:
                    rightSide = node
                    que.append(node.left)
                    que.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res