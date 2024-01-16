class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.prefix_mat = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                upper = 0
                left = 0
                middle = 0

                if r - 1 >= 0:
                    left = self.prefix_mat[r - 1][c]
                if c - 1 >= 0:
                    upper = self.prefix_mat[r][c - 1]
                if c - 1 >= 0 and r - 1 >= 0:
                    middle = self.prefix_mat[r - 1][c - 1]

                self.prefix_mat[r][c] = left + upper - middle + matrix[r][c]
                # print(r,c)
        # print(self.prefix_mat)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left = 0
        upper = 0
        middle = 0

        if col1 - 1 >= 0:
            left = self.prefix_mat[row2][col1-1]
        if row1 - 1 >= 0:
            upper = self.prefix_mat[row1-1][col2]
        if row1 - 1 >= 0 and col1 - 1 >= 0:
            middle = self.prefix_mat[row1 - 1][col1 - 1]

        return self.prefix_mat[row2][col2] - left - upper + middle
        # return 0
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
