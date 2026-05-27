# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 
        res = root.val
        def dfs(root):
            nonlocal res
            if not root: return 0
            leftNode = dfs(root.left)
            rightNode = dfs(root.right)

            left = max(leftNode, 0)
            right = max(rightNode, 0)
            res = max(res, root.val + left+right)
            return root.val + max(left, right)
        dfs(root)
        return res
        