class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = []
        for i in range(len(board)):
            rows.append(set())
        cols = []
        for i in range(len(board)):
            cols.append(set())
        squares = []
        for i in range(len(board)):
            squares.append(set())

        for i in range(len(board)):
            for j in range(len(board[i])):
                val = board[i][j]
                square = ((3 * (i // 3)) + (j // 3))

                if val != '.' and (
                    val in rows[i] or
                    val in cols[j] or
                    val in squares[square]
                ):
                    return False
                
                rows[i].add(val)
                cols[j].add(val)
                squares[square].add(val)
        
        return True