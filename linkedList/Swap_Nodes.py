# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
 1 -> 2
 2 -> 1

 first -> last
 last points to first
 first points to the next of last after reversing

"""
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time: O(n)
        Space: O(1)
        """
        if not head or not head.next:
            return head
        curr = head.next
        prev = head
        head = head.next
        temp = curr
        while curr and curr.next:
            curr.next, prev.next = prev, curr.next
            temp = prev
            prev = prev.next
            if prev:
                curr = prev.next
                temp.next = curr if curr else prev
        if prev.next:
            curr.next, prev.next = prev, None
        return head