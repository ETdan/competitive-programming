# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False
        
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    if row == 0:
                        first_row_has_zero = True
                    if col == 0:
                        first_col_has_zero = True
                    matrix[row][0] = matrix[0][col] = 0

        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
        
        if first_row_has_zero:
            for col in range(cols):
                matrix[0][col] = 0
        
        if first_col_has_zero:
            for row in range(rows):
                matrix[row][0] = 0
