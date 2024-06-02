# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        memo = {}
        
        def dp(row, col):
            if row == len(matrix) or col == len(matrix[0]):
                return 0
        
            if (row, col) not in memo:
                toDiag = dp(row + 1, col + 1)            
                toBottom = dp(row + 1, col)
                toRight = dp(row, col + 1)
                
                if matrix[row][col] == "1":
                    memo[(row, col)] = 1 + min(toRight, toBottom, toDiag)
                else:
                    memo[(row, col)] = 0

            return memo[(row, col)]
        
        dp(0,0)
        
        return max(memo.values()) ** 2