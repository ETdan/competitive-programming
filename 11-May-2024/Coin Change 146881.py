# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo=defaultdict(int)
        # coins.sort(reverse=True)

        def dp(target):
            if target in memo:
                return memo[target]
                
            if target == 0:
                return 0
            elif target < 0:
                return float('inf')
            
            answer = float("inf")
            for coin in coins:
                answer =min(answer ,dp(target - coin) + 1)
            
            memo[target] = answer
            return memo[target]  
                
        answer = dp(amount)

        return answer if answer != float('inf') else -1