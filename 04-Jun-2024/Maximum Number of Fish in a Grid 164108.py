# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        q = deque()
        answer = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def bfs(i, j):
            nonlocal answer
            temp = 0
            q.append((i, j))

            while q:
                row, col = q.popleft()
                temp += grid[row][col]
                grid[row][col] = 0

                for rowChange, colChange in directions:
                    new_row = row + rowChange
                    new_col = col + colChange

                    if inbound(new_row, new_col) and grid[new_row][new_col] > 0:
                        q.append((new_row, new_col))

            answer = max(answer, temp)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]>0:
                    bfs(i, j)

        return answer
