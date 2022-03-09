# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        visited = set()
        visited.add(root)
        ans = []
        while queue:
            levelSum = 0
            n = len(queue)
            
            for i in range(n):
                node = queue.popleft()
                levelSum += node.val
                if node.left:
                    queue.append(node.left)
                    visited.add(node.left)
                if node.right:
                    queue.append(node.right)
                    visited.add(node.right)
            ans.append(levelSum/n)
        
        return ans
