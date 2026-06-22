# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:           

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        for i in range(1, len(lists)):
            lists[i] = self.mergeLists(lists[i - 1], lists[i])
        return lists[-1]

    def mergeLists(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l2.val < l1.val:
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next
            tail = tail.next 
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next