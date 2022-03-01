# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        ans = []
        visited = set()
        temp = root

        while stack:
            if stack[-1] == None:
                stack.pop()
            elif  stack[-1] not in visited:
                visited.add(stack[-1])
                stack.append(stack[-1].left)
            else:
                node = stack.pop()
                ans.append(node.val)
                if node.right:
                    stack.append(node.right)

        return ans











# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def traverse(node):
            if node != None:
                traverse(node.left)
                ans.append(node.val)
                traverse(node.right)
        
        traverse(root)
        return ans
            
