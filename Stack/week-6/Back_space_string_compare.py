class Solution:
    def deleted_string(self, s: str) -> str:
        stack = []
        for i in s:
            if stack and i == '#':
                stack.pop()
            if i != '#':
                stack.append(i)
        return ''.join(stack)
    def backspaceCompare(self, s: str, t: str) -> bool:
        """  
        """
        return self.deleted_string(s) == self.deleted_string(t)
