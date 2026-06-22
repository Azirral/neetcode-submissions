# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Input: list1, list2 - two lists sorted ascendingly
        # Output: merged - input lists merged and sorted ascendingly
        # Approach:
        # If one of the lists is empty, return the other
        # Iterate through both lists
        # Keep track of the merged list current value
        # Keep track of the head of the merged list
        # Add the smaller equal node to the merged, and update the pointers
        # If one of the lists becomes empty, then add the remaining list to the end of the merged and return
        if not(list1):
            return list2
        elif not(list2):
            return list1

        merged = None
        curr = None
        if list1.val <= list2.val:
            merged = list1
            curr = list1
            temp = list1.next
            list1 = temp
        else:
            merged = list2
            curr = list2
            temp = list2.next
            list2 = temp
        merged.next = None
        curr.next = None
        while list1 and list2:
            if list1.val <= list2.val:
                temp = list1.next
                curr.next = list1
                curr = curr.next
                list1 = temp
            else:
                temp = list2.next
                curr.next = list2
                curr = curr.next
                list2 = temp

        if not(list1):
            curr.next = list2
            return merged
        elif not(list2):
            curr.next = list1
            return merged

        


