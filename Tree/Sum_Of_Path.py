# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def sumN(node):
            if node == None:
                return []
            if node.left == node.right == None:
                return [str(node.val)]
            left = sumN(node.left)
            right = sumN(node.right)
            ans = left + right
            i = 0
            while i < len(ans):
                ans[i] = str(node.val) + ans[i]
                i+=1
            return ans
        sumOfPath = sumN(root)
        return sum(list(map(int, sumOfPath)))
