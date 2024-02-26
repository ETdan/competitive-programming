class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length=len(nums)
        max_=0
        
        for i in range(length):
            if i > max_:
                return False
            if i + nums[i] > max_:
                max_=i+nums[i]

        return True