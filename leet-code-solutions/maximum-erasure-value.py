class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        pre_sum=0
        left=0
        contained_values=set()
        max_score=0

        for right in range(len(nums)):
            pre_sum += nums[right]
            if nums[right] in contained_values:
                value_to_remove = nums[right]
                
                while value_to_remove != nums[left]:
                    contained_values.remove(nums[left])  
                    pre_sum -= nums[left]
                    left+=1

                # contained_values.remove(nums[left])  
                pre_sum -= nums[left]
                left+=1
                
            else:
                contained_values.add(nums[right])
                max_score=max(max_score,pre_sum)

        return max_score