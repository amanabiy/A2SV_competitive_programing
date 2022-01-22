class Solution:
    def minOperations(self, logs: List[str]) -> int:
        """ Browse folders
        Time: O(n)
        Space: O(n)
        """
        stack = []
        for i in logs:
            if stack and i == '../':
                stack.pop()
            if i != './' and i != '../':
                stack.append(i)                
        return len(stack)
