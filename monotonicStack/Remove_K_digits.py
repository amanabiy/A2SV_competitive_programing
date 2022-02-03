class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        stack is decreasing
        Time: O(1)
        space: O(1)
        """
        saved = []
        count = 0
        if len(num) == k:
            return "0"
        for n in num:
            if saved and count < k and n < saved[-1]:
                while count < k and saved and n < saved[-1]:
                    saved.pop()
                    count += 1
            saved.append(n)
        while saved and count < k:
            saved.pop()
            count += 1
        return str(int("".join(saved)))
