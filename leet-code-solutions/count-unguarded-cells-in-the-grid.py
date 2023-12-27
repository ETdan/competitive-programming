class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # grid=[[0]*m]*n
        grid=[[0]*n for _ in range(m)]

        for r,c in walls:
            grid[r][c]=2

        for r,c in guards:
            grid[r][c]=3

        for guard in guards:
            # up
            r,c = guard[0] - 1,guard[1]
            for r in range( r ,-1, -1):
                if grid[r][c] != 2 and grid[r][c] != 3:
                    grid[r][c] = 1 
                else:
                    break

                # print(*grid,"here",guard[0],guard[1])
            
            # down
            r,c = guard[0] + 1,guard[1]
            for r in range (r,len(grid)):
                if grid[r][c] != 2 and grid[r][c] != 3:
                    grid[r][c] = 1
                else:
                    break

            # right
            r,k = guard[0],guard[1] + 1
            for column in range(k, len(grid[0])):
                if grid[r][column] != 2 and grid[r][column] != 3:
                    grid[r][column] = 1 
                else:
                    break

            # # left
            r,c = guard[0],guard[1] -1
            for c in range( c ,-1, -1):
                if grid[r][c] != 2 and grid[r][c] != 3:
                    grid[r][c] = 1
                else:
                    break

        # print(*grid)

        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    counter+=1

        return counter