# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lst1, lst2 = l1, l2
        data1 = data2 = ""
        while lst1:
            data1 += str(lst1.val)
            lst1 = lst1.next
        
        while lst2:
            data2 += str(lst2. val)
            lst2 = lst2.next
        
        total_sum = int(data1[::-1]) + int(data2[::-1])

        # total_sum = int(total_sum[::-1])
        print(total_sum)
        head = dummy = ListNode(-1)
        n = len(str(total_sum))
        while n:
            new = ListNode(total_sum % 10)
            head.next = new
            total_sum //=10
            head = head.next
            n-=1
            print(total_sum)
        return dummy.next
        