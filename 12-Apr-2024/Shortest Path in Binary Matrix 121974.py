# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [
            (1, 1),
            (-1, -1),
            (0, 1),
            (1, 0),
            (-1, 0),
            (0, -1),
            (1, -1),
            (-1, 1),
        ]
        if grid[0][0] == 1:
            return -1
        
        if len(grid) == 1:
            return 1

        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid)

        short_path = 0
        q = deque()
        visited = set()
        q.append((0, 0))

        while q:
            short_path += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for change_r, change_c in directions:
                    new_r = change_r + r
                    new_c = change_c + c
                    if (new_r, new_c) in visited:
                        continue

                    if inbound(new_r, new_c) and grid[new_r][new_c] != 1:
                        # print(new_r, new_c)
                        visited.add((new_r, new_c))
                        q.append((new_r, new_c))
                        if (new_r, new_c) == (len(grid) - 1, len(grid) - 1):
                            return short_path + 1
        return -1
