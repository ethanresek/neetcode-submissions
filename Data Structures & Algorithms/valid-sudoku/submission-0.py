class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        board_map = {
            0: (0, 3),
            2: (0, 3),
            1: (0, 3),
            4: (3, 6),
            5: (3, 6),
            3: (3, 6),
            7: (6, 9),
            8: (6, 9),
            6: (6, 9),
        }
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    if (board[i][j] in board[i][:j] or 
                    board[i][j] in board[i][j + 1:]):
                        return False
                    
                    if board[i][j] in [row[j] for idx, row in enumerate(board) if i != idx]:
                        return False
                    
                    x_group = board_map[j]
                    y_group = board_map[i]
                    print(board[i][j])
                    print([row[x_group[0]: x_group[1]] for row in board[y_group[0]:y_group[1]]])

                    for line in [row[x_group[0]: x_group[1]] for row in board[y_group[0]:y_group[1]]]:
                     print(line)
                     if board[i][j] in line and j % 3 != line.index(board[i][j]):
                        return False
        
        return True

