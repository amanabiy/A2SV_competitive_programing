# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node, height):
            if not node :
                return (True, height - 1)
            
            if not node.right and not node.left:
                return (True,height)
        
            left=helper(node.left, height + 1)
            right=helper(node.right, height + 1)
            
            diff= abs(left[1] - right[1])
            if left[0] and right[0]:
                if diff <= 1:
                    return (True,max(left[1], right[1]))
            
            return (False,0)
            
        return helper(root,0)[0]
                
        
