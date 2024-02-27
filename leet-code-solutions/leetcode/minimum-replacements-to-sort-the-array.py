class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        answer=0
        
        for i in range(len(nums)-1,0,-1):
            if nums[i] < nums[i-1]:
                k=ceil(nums[i-1]/nums[i])
                answer += k-1
                nums[i-1]=floor(nums[i-1]/k)
        
        return answer