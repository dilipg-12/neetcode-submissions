# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True

        def check_balance(root):
            if not root: return 0
            l = check_balance(root.left)
            r = check_balance(root.right)

            if abs(l-r) > 1:
                self.res = False
            return 1 + max(l, r)
        check_balance(root)
        return self.res