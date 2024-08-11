# Problem: Minimum Difference Between Largest and Smallest Value in 3 Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <5:
            return 0

        nums.sort()
        j=-4
        min_=float('inf')

        for i in range(4):
            min_=min(min_,nums[j]-nums[i])
            j+=1

        return min_