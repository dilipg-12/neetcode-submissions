# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        lst = [root]
        res = []
        while lst:
            t = True
            n = len(lst)
            # for i in range(n, -1, -1):
            for i in range(n):
                node = lst.pop()
                if t:
                    res.append(node.val)
                    t = False
                if node.right:
                    lst.insert(0, node.right)
                if node.left:
                    lst.insert(0, node.left)
        return res



        