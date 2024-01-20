class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        pre_sum = sum(nums)
        remainder = pre_sum % p

        if remainder == 0:
            return 0
       
        pre_sum = 0
        min_len = len(nums)
        counter={0:-1}

        for i,num in enumerate(nums):
            pre_sum += num
            pre_sum %= p
            target =  (pre_sum - remainder + p) % p

            if target in counter:
                min_len = min(min_len, i - counter[target])

            counter[pre_sum] = i

        return -1 if min_len == len(nums) else min_len
