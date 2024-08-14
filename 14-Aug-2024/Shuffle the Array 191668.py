# Problem: Shuffle the Array - https://leetcode.com/problems/shuffle-the-array/

class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        n1=nums[:n]
        n2=nums[n:]
        answer=[]
        
        for i in range(len(nums)):
            if i < len(n1):
                answer.append(n1[i])
            if i < len(n1):
                answer.append(n2[i])
        
        return answer
        