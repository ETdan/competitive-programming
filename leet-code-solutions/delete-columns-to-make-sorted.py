class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        answer=[]
        counter=0

        for i in range(len(strs[0])):
            cols=[]
            for j in range(len(strs)):
                cols.append(strs[j][i])
            answer.append(cols)
        
        for col in answer:
            if col != sorted(col):
                counter+=1
        
        return counter