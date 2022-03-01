# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left == root.right == None:
            return True
        if not root.left or not root.right:
            return False
        que = deque()
        left = root.left
        right = root.right
        if left.val != right.val:
            return False
        que.append(left)
        que.append(right)
        while que:
            left = que.popleft()
            right = que.popleft()
            l_lchild = left.left
            l_rchild = left.right
            r_lchild = right.left
            r_rchild = right.right
            if l_lchild or r_rchild:
                if not l_lchild or not r_rchild or l_lchild.val != r_rchild.val:
                    return False
            if l_rchild or r_lchild:
                if not l_rchild or not r_lchild or l_rchild.val != r_lchild.val:
                    return False
            if l_rchild:
                que.append(l_rchild)
                que.append(r_lchild)
            if l_lchild:
                que.append(l_lchild)
                que.append(r_rchild)
        return True
