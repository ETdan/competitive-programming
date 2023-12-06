class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        Dict={}
        answer=[]
        n=floor(len(nums)/3)

        for i in nums:
            if i in Dict:
                Dict[i]+=1
            else:
                Dict[i]=1
        
        for key,val in Dict.items():
            if val > n:
                answer.append(key)

        return answer

        