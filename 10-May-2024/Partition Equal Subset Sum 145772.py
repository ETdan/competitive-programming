# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)

        if target % 2 != 0:
            return False

        target //= 2

        memo = {}

        def dp(i, targetSum):
            if i == len(nums) or targetSum == target:
                return targetSum == target

            elif (i, targetSum) not in memo:
                memo[(i, targetSum)] = dp(i + 1, targetSum + nums[i]) or dp(
                    i + 1, targetSum
                )

            return memo[(i, targetSum)]

        return dp(0, 0)

        # memo=defaultdict(bool)
        # def dp(i,sumA,sumB):
        #     if i == len(nums):
        #         return sumA == sumB
        #     else:
        #         if (i,sumA,sumB) not in memo:
        #             memo[(i,sumA,sumB)] = dp(i+1,sumA+nums[i],sumB) or dp(i+1,sumA,sumB+nums[i])

        #     return memo[(i,sumA,sumB)]

        # return dp(0,0,0)
