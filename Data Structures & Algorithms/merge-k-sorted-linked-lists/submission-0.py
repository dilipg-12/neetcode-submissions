# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        print(lists)
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                lst1 = lists[i]
                lst2 = lists[i + 1] if (i+1) < len(lists) else None
                merged.append(self.mergelists(lst1, lst2))
            lists = merged
        return lists[0]

    def mergelists(self, lst1, lst2):
        n = dummy = ListNode(0)
        while lst1 and lst2:
            if lst1.val < lst2.val:
                n.next = lst1
                lst1 = lst1.next
            else:
                n.next = lst2
                lst2 = lst2.next
            n = n.next
        n.next = lst1 or lst2
        return dummy.next
        