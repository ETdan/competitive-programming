# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums=[str(num) for num in nums]

        def helper(num1,num2):
            if int(num1 + num2) < int(num2 + num1):
                return [num2, num1]
            else:
                return [num1, num2]
                

        for i in range(len(nums)):
            for j in range(len(nums)-1-i):
                nums[j], nums[j+1] = helper(nums[j],nums[j+1])
                # print(nums[j], nums[j+1])

        answer="".join(nums)
        if "0"*len(nums) == answer:
            return "0" 
        return answer 

        