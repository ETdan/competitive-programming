# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dp(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in memo:
                return memo[(i, buying)]

            if buying:
                buy = dp(i + 1, not buying) - prices[i]
                cooldown = dp(i + 1, buying)
                memo[(i, buying)] = max(buy,cooldown)
            else:
                sell = dp(i + 2, not buying) + prices[i]
                cooldown = dp(i + 1,  buying)
                memo[(i, buying)] = max(sell,cooldown)
                
            
            return memo[(i,buying)]
        
        return dp(0,True)