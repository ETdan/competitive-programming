class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        posetive_list=[]
        negative_list=[]
        answer=[]

        for i in range(len(nums)):
            if nums[i] < 0:
                negative_list.append(nums[i])
            else:
                posetive_list.append(nums[i])
        
        for i in range(len(posetive_list)):
            answer.append(posetive_list[i])
            answer.append(negative_list[i])
            
        return answer