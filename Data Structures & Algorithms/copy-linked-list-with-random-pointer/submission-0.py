"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cc = {None: None}
        f = head
        while f:
            new = Node(f.val)
            cc[f] = new
            f = f.next
        f = head
        while f:
            cc[f].next = cc[f.next]
            cc[f].random = cc[f.random]
            f = f.next


        ll = cc[head]
        return ll


        