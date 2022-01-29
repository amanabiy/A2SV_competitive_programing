# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """ add two linked list
        Time: O(n)
        Space: O(n)
        """
        remainder = 0
        ans2 = ListNode()
        while l1 or l2:
            ans = remainder
            if l1:
                ans += l1.val
                l1 = l1.next
            if l2:
                ans += l2.val
                l2 = l2.next
            if ans >= 10:
                remainder = 1
            else:
                remainder = 0
            ans = ans % 10
            self.insertLinkedList(ans2, ans)
        if remainder != 0:
            self.insertLinkedList(ans2, remainder)
        return ans2.next

    def insertLinkedList(self, head, val):
        """ insert a value at the end of a linkedList
        Time: O(n)
        Space:O(1)
        """
        temp = head
        if not temp:
            temp = ListNode(val)
        while temp.next:
            temp = temp.next
        temp.next = ListNode(val)
        
                
