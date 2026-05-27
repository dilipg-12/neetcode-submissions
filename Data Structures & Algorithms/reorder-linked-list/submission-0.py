# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None

        prev = None
        while second:
            nt = second.next
            second.next = prev
            prev = second
            second = nt
        first, last = head, prev
        while last:
            tmp1, tmp2 = first.next, last.next

            first.next = last
            last.next = tmp1

            first, last = tmp1, tmp2

        