# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.total_sum = 0
        
        def findValues(node, parent, grandParent):
            if not node:
                return

            findValues(node.left, node, parent)
            findValues(node.right, node, parent)
            
            if grandParent and grandParent.val % 2 == 0:
                self.total_sum += node.val
            
            
        findValues(root, None, None)
        return self.total_sum
