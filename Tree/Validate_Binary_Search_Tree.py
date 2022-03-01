# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Time: O(n)
        Space: O(1) function callstack O(n)
        """
        def dfs(node, large, small):
            if not node:
                return True
            if node.val >= large:
                return False
            if node.val <= small:
                return False
            left = dfs(node.left, node.val, small)
            right = dfs(node.right, large, node.val)
            return left and right
            
        return dfs(root, float('inf'), float('-inf'))
        
