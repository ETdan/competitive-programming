# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dp(i, buying, k):
            if (i, buying,k) in memo:
                return memo[(i, buying,k)]

            if i == len(prices) or k == 0:
                return 0

            if buying:
                memo[(i, buying,k)] = max(dp(i + 1, False, k) - prices[i], dp(i + 1, True, k))
            else:
                memo[(i, buying,k)] = max(dp(i + 1, True, k-1) + prices[i], dp(i + 1, False, k))

            return memo[(i, buying,k)]

        return dp(0, True, 1)
