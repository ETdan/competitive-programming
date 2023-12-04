class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_con=0
        count=0
        for num in nums:
            if num==1:
                count+=1
            else:
                max_con=max(max_con,count)
                count=0
        max_con=max(max_con,count)
        return max_con