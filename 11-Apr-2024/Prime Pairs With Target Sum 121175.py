# Problem: Prime Pairs With Target Sum - https://leetcode.com/problems/prime-pairs-with-target-sum/description/

class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        
        def prime_sieve(n):
            is_prime = [True for _ in range(n + 1)]
            is_prime[0] = is_prime[1] = False
            i = 2
            while i <= n:
                if is_prime[i]:
                    j = 2 * i
                while j <= n:
                    is_prime[j] = False
                    j += i
                i += 1
            return is_prime
        
        is_prime = prime_sieve(n)

        answer=[]

        for i in range(2,n//2+1):
            if is_prime[i] and is_prime[n-i]:
                answer.append([i,n-i])
        
        
        return answer