class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = []
        cols = []
        squares = []

        for _ in range(9):
            rows.append(set())
            cols.append(set())
            squares.append(set())
        
        for row in range(len(board)):
            for col, val in enumerate(board[row]):

                square = (row // 3) * 3 + (col // 3)

                if (val != "." and (
                    val in rows[row] or
                    val in cols[col] or
                    val in squares[square])):

                    return False
                
                rows[row].add(val)
                cols[col].add(val)
                squares[square].add(val)
        
        return True