# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        total = 0

        while curr:
            total += 1
            curr = curr.next

        while total >= k:
            count = 0
            curr = prev.next
            nxt = curr.next
            while count < k - 1:
                curr.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
                nxt = curr.next
                count += 1
            prev = curr
            total -= k
        return dummy.next
