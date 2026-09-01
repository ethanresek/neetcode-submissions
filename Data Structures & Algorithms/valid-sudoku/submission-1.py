class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = []
        cols = []
        squares = []

        for i in range(9):
            rows.append(set())
            cols.append(set())
            squares.append(set())
        
        for row in range(len(board)):
            for col in range(len(board[i])):
                i = (row // 3) * 3 + (col // 3)
                val = board[row][col]


                if (val != "." and
                    (val in rows[row] or
                    val in cols[col] or
                    val in squares[i])):
                    print(val)
                    return False
                rows[row].add(val)
                cols[col].add(val)
                squares[i].add(val)
        
        return True