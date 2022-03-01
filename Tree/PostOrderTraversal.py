# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        ans = []
        visited_right = set()
        visited_left = set()
        temp = root

        while stack:
            if stack[-1] == None:
                stack.pop()
            elif stack[-1]  in visited_right and stack[-1] in visited_left:
                value = stack.pop()
                ans.append(value.val)
            elif  stack[-1] and stack[-1] not in visited_left:
                visited_left.add(stack[-1])
                stack.append(stack[-1].left)
            elif stack[-1] not in visited_right:
                node = stack[-1]
                visited_right.add(stack[-1])
                stack.append(node.right)
                    

        return ans
            
