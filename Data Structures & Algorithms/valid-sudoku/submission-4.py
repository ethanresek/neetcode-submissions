class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = []
        cols = []
        squares = []

        for _ in range(len(board)):
            rows.append(set())
            cols.append(set())
            squares.append(set())

        for i in range(len(board)):
            for j, val in enumerate(board[i]):
                
                sqr_pos = (i // 3) * 3 + (j // 3)
                
                if (val != "." and (
                    val in rows[i] or
                    val in cols[j] or
                    val in squares[sqr_pos]
                )):
                    return False
                
                rows[i].add(val)
                cols[j].add(val)
                squares[sqr_pos].add(val)

        return True