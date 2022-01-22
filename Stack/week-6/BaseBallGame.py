class Solution:
    def calPoints(self, ops: List[str]) -> int:
        """ Keep track of records
        Time: O(n)
        Space: O(n)
        """
        points = []
        for i in ops:
            if i == "+":
                y = points.pop()
                x = points.pop()
                points.extend([x, y, x + y])
            elif i == "D":
                y = points[-1] * 2
                points.append(y)
            elif i == "C":
                points.pop()
            else:
                i = int(i)
                points.append(i)
        return sum(points)
