# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache={}
        def dp(i,k):
            if (i,k) in cache:
                return cache[(i,k)]
            if i>len(coins)-1:
                cache[(i,k)]=0
                return 0
            if k<0:
                cache[(i,k)]=0
                return 0
            if k==0:
                cache[(i,k)]=1
                return 1
            take=dp(i,k-coins[i])
            ntake=dp(i+1,k)
            cache[(i,k)]=take+ntake
            return take+ntake
        return dp(0,amount)