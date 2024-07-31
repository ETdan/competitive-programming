# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums)<2:
            return 0

        max=0
        nums.sort()

        for i in range(len(nums)-1,0,-1):
            if max < nums[i] -nums [i-1]:
                max= nums[i] -nums [i-1]

        return max