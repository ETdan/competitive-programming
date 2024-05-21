# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1]:
            return 0

        def inBound(i, j):
            if 0 <= i < len(obstacleGrid) and 0 <= j < len(obstacleGrid[0]):
                return True
            else:
                return False

        for i in range(len(obstacleGrid) - 1, -1, -1):
            for j in range(len(obstacleGrid[0]) - 1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = "a"

        obstacleGrid[-1][-1] =1

        for i in range(len(obstacleGrid) - 1, -1, -1):
            for j in range(len(obstacleGrid[0]) - 1, -1, -1):
                if obstacleGrid[i][j] != "a":
                    down = up = 0
                    if inBound(i + 1, j) and obstacleGrid[i + 1][j] != "a":
                        down = obstacleGrid[i + 1][j]
                    if inBound(i, j + 1) and obstacleGrid[i][j + 1] != "a":
                        up = obstacleGrid[i][j + 1]

                    obstacleGrid[i][j] += down + up

        return obstacleGrid[0][0]
