class Solution:
    def fib(self, n: int) -> int:
        """ fibonachi numbers 
        Time: O(2^n)
        Space: O(1)
        """
        if n == 1:
            return 1
        if n == 0:
            return 0
        return self.fib(n-1) + self.fib(n-2)
