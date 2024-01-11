class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left=0

        zero_count=0
        one_count=0

        max_count=0


        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            if zero_count < 2:
                max_count = max(max_count,right-left)
            else:
                if nums[left] == 0:
                    zero_count -= 1

                left += 1

        return max_count