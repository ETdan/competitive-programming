class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer=[]
        temp=[]
        seen=set()

        def recur(left):
            nonlocal seen
            # print(candidates[left:],seen,left)
            if temp and tuple(sorted(temp)) in seen:
                return
            seen.add(tuple(sorted(temp)))

            sum_ = sum(temp)
            if sum_ == target:
                # seen.add(tuple(sorted(temp)))
                answer.append(temp[:])
                return
            elif sum_ > target:
                return

            for i in range(left,len(candidates)):
                temp.append(candidates[i])
                recur(i+1)
                temp.pop()  
        
        recur(0)
        return answer