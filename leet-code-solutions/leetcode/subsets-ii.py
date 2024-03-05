class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        answer=[]
        temp=[]
        seen=set()

        def recur(left):
            if tuple(sorted(temp[:])) not in seen:
                answer.append(temp[:])
                seen.add(tuple(sorted(temp[:])))
            

            for i  in range(left,len(nums)):
                temp.append(nums[i])
                recur(i+1)
                temp.pop()                                                          
        

        recur(0)
        
        return answer