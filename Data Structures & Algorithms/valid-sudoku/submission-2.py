class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = []
        columns = []
        squares = []

        for _ in range(9):
            rows.append(set())
            columns.append(set())
            squares.append(set())

        for i in range(len(board)):
            for j, val in enumerate(board[i]):

                sqr_num = (i // 3) * 3 + (j // 3)
                if (val != "." and
                    (val in rows[i] or
                    val in columns[j] or
                    val in squares[sqr_num])):
            
                    return False

                rows[i].add(val)
                columns[j].add(val)
                squares[sqr_num].add(val)

        return True
