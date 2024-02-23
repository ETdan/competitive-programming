class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        answer = presum = nums[0]

        for i in range(1, len(nums)):
            presum += nums[i]
            answer = max(answer, math.ceil(presum / (i + 1)))

        return answer
