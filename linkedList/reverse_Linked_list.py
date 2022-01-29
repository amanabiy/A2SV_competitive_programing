# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ reverse a linked list
        Time: O(1)
        space: O(1)
        """
        count = 0
        temp1 = temp2 = temp3 = head
        
        if not temp1:
            return temp1

        if temp1.next:
            temp3 = temp1.next
            temp1.next = None
        else:
            return temp1
        
        while temp3:
            temp2 = temp3
            temp3 = temp3.next
            temp2.next = temp1
            temp1 = temp2
        return temp2
            
            
        
