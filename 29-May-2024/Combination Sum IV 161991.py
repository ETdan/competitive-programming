# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(target):
            if target in memo:
                return memo[target]

            if target <= 0:
                if target == 0:
                    return 1
                else:
                    return 0
            answer=0
            for index in range(len(nums)):
                answer += dp(target - nums[index])

            memo[target] = answer
            return memo[target]
        
        return dp(target)

