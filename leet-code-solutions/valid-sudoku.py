class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row=defaultdict(set)
        col=defaultdict(set)
        squares=defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in squares[(r//3, c//3)]:
                        return False
                    else:
                        squares[(r//3, c//3)].add(board[r][c])
                        row[r].add(board[r][c])
                        col[c].add(board[r][c])

        return True