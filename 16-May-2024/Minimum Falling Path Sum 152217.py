# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def inbound(i,j):
            if 0 <= i < len(matrix) and 0 <= j < len(matrix):
                return matrix[i][j]
            else:
                return float('inf')

        for i in  range(1,len(matrix)):
            for j in  range(len(matrix)):
                matrix[i][j]+=min(inbound(i-1,j),inbound(i-1,j-1),inbound(i-1,j+1))
        
        return min(matrix[-1])