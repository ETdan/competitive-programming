# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def bfs(r, c):
		
            q = deque([(r,c)])
            while q:        
                r, c = q.popleft()
                if board[r][c] == 'O':
                    board[r][c] = 'N'
                    for dr, dc in [[r+1,c], [r-1,c], [r,c+1], [r,c-1]]:
                        if (dr in range(len(board)) and dc in range(len(board[0])) and board[dr][dc] == 'O'):
                            q.append((dr, dc))
        
        
        n, m = len(board), len(board[0])
        
        for i in range(m):
            if board[0][i] == 'O': bfs(0, i)
            if board[n-1][i] == 'O': bfs(n-1, i)
                
        for i in range(n):
            if board[i][0] == 'O': bfs(i, 0)
            if board[i][m-1] == 'O': bfs(i, m-1)
    
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'X': continue
                elif board[i][j] == 'N': board[i][j] = 'O' 
                else: board[i][j] = 'X'
                