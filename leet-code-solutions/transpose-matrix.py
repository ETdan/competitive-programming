class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        answer=[]

        for j in range(len(matrix[0])):
            col=[]
            for i in range(len(matrix)):
                col.append(matrix[i][j])
            answer.append(col)
        
        return answer