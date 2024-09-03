# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < k:
            k = k%len(nums)
        # rotation = ceil(len(nums)//k)

        rotated_nums=nums[-k:]
        for i in range(len(nums)-k-1,-1,-1):
            nums[i+k]=nums[i]
        # print(rotated_nums,k+1)
        for i in range(len(rotated_nums)):
            nums[i]=rotated_nums[i]
