class Solution:
    reverse=0
    def kthGrammar(self, n: int, k: int) -> int:

        def recur(n, k):
            if n == 1:
                return self.reverse
            
            if pow(2,n-1)//2 - k < 0:
                self.reverse+=1
                k = abs(pow(2,n-1)//2 - k)
            return recur(n - 1, k)

            
                
        return recur(n,k) % 2
