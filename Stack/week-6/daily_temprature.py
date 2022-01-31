class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """ 
        """
        stack = []
        dtemp = [0] * len(temperatures) 
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                val, j = stack.pop()
                dtemp[j] = i - j 
            stack.append((temp, i))
        return dtemp
