# Problem: Find the Duplicate Number - https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]

        # for i in range(len(nums)):
        #     left_index=bisect_left(nums,nums[i])
        #     right_index=bisect_right(nums,nums[i])
        #     print(left_index,right_index,nums[i])
        #     if right_index - left_index > 1:
        #         return nums[i]
        # return 0