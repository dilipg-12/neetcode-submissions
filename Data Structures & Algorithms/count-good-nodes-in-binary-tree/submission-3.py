# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # def dfs(root, maval):
        #     if not root: return 0
        #     res = 1 if root.val >= maval else 0
        #     maval = max(maval, root.val)
        #     res += dfs(root.left, maval)
        #     res += dfs(root.right, maval)
        #     return res
        # return dfs(root, root.val)
        res = 0
        # lst = deque((root, root.val))
        lst = deque()
        lst.append((root, root.val))
        while lst:
            node, maval = lst.popleft()
            if node.val >= maval:
                res += 1
            if node.left:
                lst.append((node.left, max(node.val, maval)))
            if node.right:
                lst.append((node.right, max(node.val, maval)))
        return res 

        