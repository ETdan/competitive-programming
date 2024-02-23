class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        prev_min = nums[0]

        for n in nums[1:]:
            while stack and n >= stack[-1][0]:
                stack.pop()

            if stack and n > stack[-1][1]:
                return True

            stack.append([n,prev_min])
            prev_min = min(prev_min, n)

        return False
