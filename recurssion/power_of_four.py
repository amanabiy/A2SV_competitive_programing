# another hint all numbers divisible with 4 have an end with 4, 8, 12 and 16

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 4:
            return False
        return self.isPowerOfFour(n/4)
        
