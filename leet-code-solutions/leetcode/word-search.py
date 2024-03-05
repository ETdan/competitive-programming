class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        moves = [[-1,0],[0,1],[1,0],[0,-1]]
        temp = []
        seen = set()
        n, m = len(board), len(board[0]) 

        def backTrack(row,col, next_char_index):
            seen.add(tuple([row,col]))
            temp.append(board[row][col])

            if len(temp) >= len(word):
                return len(temp) == len(word)

            for move in moves:
                next_row = row + move[0]
                next_col = col + move[1]

                if 0 <= next_row < n and 0 <= next_col < m:
                    if word[next_char_index +1] == board[next_row][next_col] and (next_row,next_col) not in seen:
                        if backTrack(next_row,next_col, next_char_index +1):
                            return True

            temp.pop()
            seen.remove((row,col))
            return False

        index=0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and backTrack(i, j, index):
                    return True
        
        return False
