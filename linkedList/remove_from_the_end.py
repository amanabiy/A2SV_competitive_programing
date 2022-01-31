# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """ remove the nth node
        Time: O(1)
        Space: O(1)
        """
        faster = head
        slower = head
        gap = n
        count = 0
        
        # check if the list is empty
        if slower.next == None:
            return faster.next
        
        if slower.next.next == None:
            if n == 1:
                slower.next = None
            if n == 2:
                slower = slower.next
            return slower
        
        # make faster go a head and 
        while count < gap:
            # remove the first element if it reached last element
            if faster.next:
                faster = faster.next
            else:
                return slower.next
            count += 1
        
        # move both until the end with the given gap
        while faster and faster.next:
            faster = faster.next
            slower = slower.next

        # remove the middle element
        temp1 = slower.next if slower else None
        slower.next = temp1.next if temp1 else None

        return head
