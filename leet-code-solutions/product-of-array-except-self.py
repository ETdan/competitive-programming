class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []

        prefix=1
        for i in range(len(nums)):
            answer.append(prefix)
            prefix*=nums[i]
        
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            answer[i]*=postfix
            postfix*=nums[i]
        
        return answer
