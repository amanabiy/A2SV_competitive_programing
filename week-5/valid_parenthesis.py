class Solution:
    def isValid(self, s: str) -> bool:
        """Check parenthesis"""
        brackets = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        check = []
        for i in s:
            if i in brackets.values():
                check.append(i)
            else:
                if check and brackets[i]  == check[-1]:
                    check.pop()
                else:
                    return False
        if len(check) == 0:
            return True
        else:
            return False
