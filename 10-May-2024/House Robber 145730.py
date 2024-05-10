# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) < 3:
            return max(nums)

        memo = {1: max(nums[0], nums[1]), 0: nums[0]}

        def dp(i):
            if i not in memo:
                memo[i] = max(nums[i] + dp(i - 2), dp(i - 1))

            return memo[i]

        return dp(len(nums) - 1)
