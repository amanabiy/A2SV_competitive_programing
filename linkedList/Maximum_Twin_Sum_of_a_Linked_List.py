# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        """
        Find the half of the linkedlist
        reverse the list after the middle
        compare each element
        Time: O(n)
        Space: O(1)
        """
        slower = faster = head
        maximum = 0
        while faster and faster.next:
            slower = slower.next
            faster = faster.next.next
        
        #reverse the list starting from slower.next
        reverse = None
        while slower:
            nexts = slower.next
            slower.next = reverse
            reverse = slower
            slower = nexts

            
        temp = head
        while temp and reverse:
            maximum = max(temp.val + reverse.val, maximum)
            temp = temp.next
            reverse = reverse.next

        return maximum