# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(i, curSum):
            if i == len(nums):
                if curSum == target:
                    return 1
                else:
                    return 0
            
            if (i,curSum) not in memo:
                memo[(i,curSum)] = dp(i + 1, curSum + nums[i]) + dp(i + 1, curSum - nums[i])
            
            return memo[(i,curSum)]
        
        return dp(0, 0)

