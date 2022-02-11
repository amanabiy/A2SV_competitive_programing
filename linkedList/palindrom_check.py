# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        faster = slower = start = head

        while faster and faster.next:
            faster = faster.next.next
            slower = slower.next
        
        middle = None
        while slower:
            if not middle:
                middle = ListNode(slower.val)
            else:
                temp = middle
                new_node = ListNode(slower.val)
                new_node.next = middle
                middle = new_node
            slower = slower.next

        while middle:
            if middle.val != start.val:
                return False
            middle = middle.next
            start = start.next
        return True
