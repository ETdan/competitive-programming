# Problem:  Frequency of the Most Frequent Element (Optional) - https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        max_freq=0
        pre_sum=0
        n=len(nums)

        left=0

        for right in range(len(nums)):
            pre_sum += nums[right]
            if nums[right] * (right - left + 1) - pre_sum > k:
                # print("here",pre_sum,nums[right])
                while left < n and (pre_sum + k) < (nums[right] * (right - left + 1)):
                    pre_sum -= nums[left]
                    left += 1

            max_freq = max(max_freq,right-left+1)


























        # for i in range(len(nums)-1,-1,-1):
        #     local_max=1
        #     val=nums[i]
        #     temp_k=k
        #     for j in range(i-1,-1,-1):
        #         temp_k -= val - nums[j]
        #         if temp_k < 0:
        #             break
        #         local_max+=1

        #     max_freq=max(max_freq,local_max)
        
        return max_freq