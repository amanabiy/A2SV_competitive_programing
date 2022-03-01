# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        ans = []
        visited = set()
        temp = root

        while stack:
            if stack[-1] == None:
                stack.pop()
            elif  stack[-1] not in visited:
                ans.append(stack[-1].val)
                visited.add(stack[-1])
                stack.append(stack[-1].left)
            else:
                node = stack.pop()
                if node.right:
                    stack.append(node.right)

        return ans
            
