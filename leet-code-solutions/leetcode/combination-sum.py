class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer=[]
        temp=[]

        def recur(left):
            sum_ = sum(temp)
            if sum_ == target:
                answer.append(temp[:])
                return
            elif sum_ > target:
                return

            for i in range(left,len(candidates)):
                temp.append(candidates[i])
                recur(i)
                temp.pop()  
        
        recur(0)
        return answer