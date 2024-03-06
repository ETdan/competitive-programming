class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        min_val = float("inf")

        while left < right:
            # print(left, right, mid)
            if mid == left or mid ==right:
                min_val= min(min_val,nums[left],nums[right])
                mid = (left + right) // 2
                
            if nums[mid] > nums[left] and nums[mid] > nums[right]:
                left = mid 
            else:
                right = mid

            min_val = min(min_val, nums[mid])

            mid = (left + right) // 2

        return min_val if len(nums) > 2 else min(nums)
