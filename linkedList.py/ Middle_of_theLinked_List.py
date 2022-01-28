# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ Better solution with two pointers
        Time: O(n)
        space: O(1)
        """
        fast = slow = head
        slowCount = fastCount = 1
        
        while fast.next:
            fast = fast.next
            fastCount += 1
            if slowCount == fastCount // 2:
                slow = slow.next
                slowCount += 1
        return slow



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ Find the elements after the middle
        Time: O(n)
        Space: O(1)
        """
        length = 0
        temp = 0
        node = head

        while node:
            length += 1
            node = node.next

        if length == 1:
            return node

        node = head
        while node:
            temp += 1
            node = node.next
            if temp == length // 2:
                return node

                
            
        