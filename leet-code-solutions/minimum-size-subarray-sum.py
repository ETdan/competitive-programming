class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr_sum=0
        min_len=float('inf')
        
        left=0
        right=0
        been_here=False

        for right in range(len(nums)):
            curr_sum += nums[right]
            
            if curr_sum >= target:
                been_here=True
                while curr_sum >= target:
                    curr_sum-=nums[left]
                    min_len=min(min_len,right-left+1)
                    left+=1
                    
        
        if been_here:
            return min_len
        else:
            return 0