class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer=[]
        for i in range(0,len(nums),2):
            f=nums[i]
            v=nums[i+1]
            for j in range(f):
                answer.append(v)
        return answer