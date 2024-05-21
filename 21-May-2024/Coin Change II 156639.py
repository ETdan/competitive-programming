# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount ==0:
            return 1

        cur=[0]*(amount+1)
        cur[0]=1

        for coin in coins:
            for i in range(len(cur)):
                if i-coin >=0:
                    cur[i]+=cur[i-coin]
        
        return cur[-1]