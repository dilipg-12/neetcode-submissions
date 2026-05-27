# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        lst1 = [p]
        lst2 = [q]

        while lst1 and lst2:
            n = len(lst1)
            p1 = lst1.pop()
            q1 = lst2.pop()
            for _ in range(n):
                if not p1 and not q1:
                    continue
                if not p1 or not q1 or (p1.val != q1.val):
                    return False
                    # break
                lst1.append(p1.left)
                lst1.append(p1.right)
                lst2.append(q1.left)
                lst2.append(q1.right)

        return not(lst1 or lst2)