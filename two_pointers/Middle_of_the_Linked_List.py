# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        slowCount = fastCount = 1
        
        while fast.next:
            fast = fast.next
            fastCount += 1
            if slowCount == fastCount // 2:
                slow = slow.next
                slowCount += 1
        return slow


                
            
        
