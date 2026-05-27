# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        lst = [root]
        # ans = [[root]]
        ans = []
        tmp = [root.val]

        while lst:
            n = len(lst)
            ans.append(tmp)
            tmp = []
            for _ in range(n):
                node = lst.pop(0)
                if node.left:
                    tmp.append(node.left.val)
                    lst.append(node.left)
                if node.right:
                    tmp.append(node.right.val)
                    lst.append(node.right)
            # print(lst)
        return ans


        