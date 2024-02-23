class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        answer = [-1] * len(nums)
        n=len(nums)
        nums+=nums

        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i%n]:
                index = stack.pop()
                answer[index%n] = nums[i%n]

            if i < n:
                stack.append(i)

        return answer
