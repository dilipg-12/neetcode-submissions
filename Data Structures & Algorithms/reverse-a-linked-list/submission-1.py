# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # h = head
        # if not(h and head.next):
        #     return h
        # p = h.next
        # while h.next:
        #     h.next = p.next
        #     p.next = head
        #     head = p
        #     p = h.next
        # return head 
        prev = None
        curr = head
        while curr:
            nt = curr.next
            curr.next = prev
            prev = curr
            curr = nt
        return prev 
        