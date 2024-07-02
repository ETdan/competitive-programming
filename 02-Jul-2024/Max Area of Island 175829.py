# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0
        
        def inbound(q, i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0 or (i, j) in visited:
                return
            q.append((i, j))
            visited.add((i, j))
            
        def bfs(i, j):
            area = 0
            q = deque()
            inbound(q, i, j)
            while q:
                for i in range(len(q)):
                    i, j = q.popleft()
                    area += 1
                    inbound(q, i + 1, j)
                    inbound(q, i - 1, j)
                    inbound(q, i, j + 1)
                    inbound(q, i, j - 1)
            return area
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    max_area = max(max_area, bfs(i, j))
                    
        return max_area