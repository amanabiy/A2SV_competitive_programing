class Solution:
    def decodeString(self, s: str) -> str:
        """ using
        Time: O(n)
        Space: O(n)
        """
        stack = []
        for l in s:
            if l.isalnum() or l == '[':
                stack.append(l)
            else:
                val = ""
                times = ""
                while not stack[-1].isdigit():
                    if stack[-1] != '[':
                        val = stack[-1] + val
                    stack.pop()
                while stack and stack[-1].isdigit():
                    times = stack.pop() + times
                stack.append(val * int(times))
        return "".join(stack)
