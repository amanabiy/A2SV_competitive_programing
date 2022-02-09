# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time: O(n)
        Space: O(1)
        """
        if not head:
            return head
        temp = head
        temp1 = head
        while temp:
            if temp.val != temp1.val:
                temp1.next = temp
                temp1 = temp1.next
            temp = temp.next
        temp1.next = None
        return head
