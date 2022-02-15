class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        return self.powerOf(5,(math.ceil(n/2)),mod) * self.powerOf(4,(n//2),mod) % mod

    def powerOf(self, n, p, modulus) -> int:
        if p == 0:
            return 1
        if p == 1:
            return n
        res = 1
        if p % 2 == 0:
            res = self.powerOf(n, p//2, modulus)
            res = res * res
        else:
            res = self.powerOf(n, (p-1), modulus) * n
        return res % modulus
