class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer=[]
        temp=[]

        def recur(left):
            answer.append(temp[:])

            for i  in range(left,len(nums)):
                temp.append(nums[i])
                recur(i+1)
                temp.pop()                                                          
        recur(0)
        return answer