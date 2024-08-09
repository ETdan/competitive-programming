# Problem: Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(1,len(grid[0])):
            grid[0][i]+=grid[0][i-1]
        
        cur = grid[0]

        for i in range(1,len(grid)):
            for j in range(len(grid[0])):
                left=grid[i][j-1] if j-1>=0 else float('inf')
                right=cur[j]
                grid[i][j]+=min(left,right)

            cur = grid[i]

        return cur[-1]