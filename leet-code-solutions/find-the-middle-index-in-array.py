class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        front_pre_sum = [0]

        for i in range(len(nums)):
            front_pre_sum.append(nums[i] + front_pre_sum[i])

        total_sum = front_pre_sum[-1]
        front_pre_sum.append(0)

        for i in range(1, len(front_pre_sum)-1):
            if total_sum - front_pre_sum[i] == front_pre_sum[i - 1]:
                return i - 1

        return -1
