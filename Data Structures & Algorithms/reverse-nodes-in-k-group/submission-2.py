# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = gprev = ListNode(-1, head)

        while True:
            kth = self.getk(gprev, k)
            if not kth:
                break
            knth = kth.next
            prev = knth
            cur = gprev.next
            while cur != knth:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            
            tmp = gprev.next
            gprev.next = kth
            gprev = tmp
        return dummy.next



    def getk(self, cur, k):
        while cur and k:
            cur = cur.next
            k -= 1
        return cur

        
        