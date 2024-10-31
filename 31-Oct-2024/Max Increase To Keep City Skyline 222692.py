# Problem: Max Increase To Keep City Skyline - https://leetcode.com/problems/max-increase-to-keep-city-skyline/

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max = [0] * len(grid)
        col_max = [0] * len(grid[0])

        for i, row in enumerate(grid):
            row_max[i] = max(row)

        for i in range(len(grid)):
            max_ = 0
            for j in range(len(grid[0])):
                if max_ < grid[j][i]:
                    max_ = grid[j][i]
                # print(grid[j][i])
            col_max[i] = max_
        # print(row_max,col_max)
        answer=0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_ = min(row_max[i],col_max[j])
                answer += max_ - grid[i][j]
        
        return answer
