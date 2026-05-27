# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return
        lst = [root]
        head = 0
        while head < len(lst):
            node = lst[head]
            if node:
                node.left, node.right = node.right, node.left
                lst.append(node.left)
                lst.append(node.right)
            head += 1
        return root


        