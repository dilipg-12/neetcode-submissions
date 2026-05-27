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

            # reverse ll logic
            prev = knth
            curr = gprev.next
            while curr != knth:
                nt = curr.next
                curr.next = prev
                prev = curr
                curr = nt
            tmp = gprev.next
            gprev.next = kth
            gprev = tmp
        return dummy.next


    def getk(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k-=1
        return curr
        