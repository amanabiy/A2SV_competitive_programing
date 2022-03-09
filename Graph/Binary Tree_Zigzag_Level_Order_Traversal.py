# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        response = []
        leftorRight = 1
        while queue:
            queueLength = len(queue)
            ans = []
            for _ in range(queueLength):
                node = queue.popleft()
                ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if leftorRight:
                leftorRight = 0
                response.append(ans)
            else:
                leftorRight = 1
                response.append(ans[::-1])
    
        return response
            
