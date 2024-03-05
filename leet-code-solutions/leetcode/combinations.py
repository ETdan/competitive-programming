class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer=[]
        comb=[]
        
        def recur(curr,k):
            if len(comb) == k:
                answer.append(comb[:])
                return

            if curr == n:
                return

            for i in range(curr+1,n+1):
                comb.append(i)
                recur(i,k)
                comb.pop()

        recur(0,k)
        return answer
