# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        q = deque()
        rotted = set()
        there_is_unrotted_orand = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    there_is_unrotted_orand = True

        if there_is_unrotted_orand:
            minutes = 0
            while q:
                minutes += 1
                for i in range(len(q)):
                    r, c = q.popleft()

                    for r_change, c_change in directions:
                        new_r = r_change + r
                        new_c = c_change + c
                        if (
                            (new_r, new_c) not in rotted
                            and inbound(new_r, new_c)
                            and grid[new_r][new_c] == 1
                        ):
                            grid[new_r][new_c] = 2
                            q.append((new_r, new_c))

            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        return -1
            else:
                return minutes - 1
        else:
            return 0
