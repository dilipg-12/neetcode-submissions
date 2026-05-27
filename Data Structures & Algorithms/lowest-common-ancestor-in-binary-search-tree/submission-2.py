# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lst = [root]
        res = lst[-1]
        if p.val > q.val:
            p,q = q,p
        while lst:
            r = lst.pop(0)
            if not r:
                break
            if (p.val <= r.val <= q.val) or (r.val <= p.val <= q.val):
                res = r
            
            if r.val < p.val:
                lst.append(r.right)
            if r.val > q.val:
                lst.append(r.left)
        return res

        