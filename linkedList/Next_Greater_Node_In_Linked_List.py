# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        """ find the lext larger of a node
        Time: O(n)
        Space: O(n)
        """
        index = 0
        stack = []
        length = self.lenList(head)
        ans = [0] * length 
        temp = head
        while temp:
            while stack and stack[-1][0] < temp.val:
                val, ind = stack.pop()
                ans[ind] = temp.val
            stack.append((temp.val, index))      
            temp = temp.next
            index += 1
        return ans

    def lenList(self, head) -> ListNode:
        if not head:
            return 0
        curr = head
        count = 0
        while curr:
            curr = curr.next
            count += 1
        return count
            
