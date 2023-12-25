class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum_=0
        j=0
        for i in range(len(mat)):
            sum_+=mat[i][i]

        for i in range(len(mat)-1,-1,-1):
            sum_+=mat[j][i]
            # print(mat[j][i])
            j+=1
        
        if len(mat) % 2 !=0:
            # print("here")
            sum_ -= mat[(len(mat)//2)][(len(mat)//2)]
        return sum_