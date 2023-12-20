class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        Dict=defaultdict(list)
        answer=[]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                Dict[i+j].append(mat[i][j])
        
        for key,val in Dict.items():
            if key % 2 == 0:
                answer.extend(val[::-1])
            else:
                answer.extend(val)

        return answer