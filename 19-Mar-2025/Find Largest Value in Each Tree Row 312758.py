# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        que = deque([root])
        ans = []

        while que:
            row_max = que[0].val
            length = len(que)
            
            for _ in range(length):
                node = que.popleft()
                row_max = max(row_max, node.val)

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            ans.append(row_max)
        return ans
                