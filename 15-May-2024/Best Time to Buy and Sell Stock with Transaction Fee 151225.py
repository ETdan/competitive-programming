# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo={}
        
        def dp(i,buying):
            if (i,buying) in memo:
                return memo[(i,buying)]

            if i == len(prices):
                return 0

            if buying:
                memo[(i,buying)] =  max(dp(i+1, False) - prices[i] - fee, dp(i+1, True))
            else:
                memo[(i,buying)] = max(dp(i+1, True) + prices[i], dp(i+1, False))
            
            return memo[(i,buying)]
        
        return dp(0,True)