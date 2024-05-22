# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}
        nums = [i for i in range(1, n)]

        def dp(i, n):
            if (i, n) in memo:
                return memo[(i, n)]

            if i == len(nums) or n <= 0:
                if n == 0:
                    return 1
                else:
                    return float("-inf")

            memo[(i, n)] = max(dp(i, n - nums[i]) * nums[i], dp(i + 1, n))
            
            return memo[(i, n)]

        return dp(0, n)
