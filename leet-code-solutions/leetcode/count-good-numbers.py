class Solution:

    def countGoodNumbers(self, n: int) -> int:
        mod= 10**9 + 7
        def myPow(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x

            if n % 2 == 0:
                res = myPow(x, n // 2)
                return res * res % mod
            else:
                res = myPow(x, (n - 1) // 2)
                return x * res * res % mod

        if n % 2 == 0:
            return myPow(20, n // 2) 
        else:
            return myPow(20, n // 2) * 5  % mod