class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        answer=[]
        even_sum=0
        for num in nums:
            if num % 2 == 0:
                even_sum+=num

        for val,index in queries:
            if nums[index] % 2 == 0:
                if (nums[index] + val) % 2 == 0:    
                    # even_sum-=nums[index]    
                    even_sum+=val    
                else: 
                    even_sum-=nums[index]    
            else:
                if (nums[index] + val) % 2 == 0:    
                    even_sum+=(val + nums[index])    

            nums[index]+=val
            answer.append(even_sum)
        
        return answer