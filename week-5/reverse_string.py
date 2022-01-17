class Solution:
    def reverseParentheses(self, s: str) -> str:
        """ reverse the string in the parenthesis
        Time: O(n)
        Space: O(n)
        """
        opening = "("
        closing = ")"
        check = []
        for letter in s:
            if letter != closing:
                check.append(letter)
            else:
                toRev = ""
                while check[-1] != opening:
                    toRev += check.pop()
                check.pop()
                for l in toRev:
                    check.append(l)
        return "".join(check)