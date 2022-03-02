# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = defaultdict(int)

        def countMode(node, count):
            if node:
                ans[node.val] += 1
                countMode(node.left, 0)
                countMode(node.right, 0)
                
        countMode(root, 0)
        maxim = max(ans.values())

        return [elem for elem in ans if ans[elem] == maxim]
