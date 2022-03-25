# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        largest = defaultdict(lambda: float('-inf'))
        
        def buildLarge(node, level):
            if node:
                if largest[level] < node.val:
                    largest[level] = node.val
                buildLarge(node.left, level + 1)
                buildLarge(node.right, level + 1)
        
        buildLarge(root, 0)
        return largest.values()
            
