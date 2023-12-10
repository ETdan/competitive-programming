class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        Dict={}

        for i in range(len(nums)):
            Dict[nums[i]]=i
        
        for operation in operations:
            item=operation[0]
            placeholder=operation[1]
            index=Dict[item]

            nums[index]=placeholder

            del Dict[item]
            
            Dict[placeholder]=index
        
        return nums 
        