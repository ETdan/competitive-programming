class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count_of_zero=0
        max_len_of_1=0
        left = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                count_of_zero += 1

            if count_of_zero > k:
                if nums[left] == 0:
                    count_of_zero -= 1
                left += 1
            max_len_of_1=max(max_len_of_1,right-left+1)
        
        return max_len_of_1