# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currVal):
            if node == None:
                return False
            if node.left == node.right == None:
                return currVal - node.val == 0
            
            return dfs(node.left, currVal - node.val) or \
                    dfs(node.right, currVal - node.val)
        
        return dfs(root, targetSum)
        
