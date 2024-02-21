class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patch = 0
        ur = 1

        i = 0
        while ur < (n + 1):
            if i < len(nums) and nums[i] <= ur:
                ur += nums[i]
                i += 1
            else:
                patch += 1
                ur *= 2
                
        return patch
