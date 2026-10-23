class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m - 1

        x = -1

        while l <= r:

            i = l + ((r - l) // 2)

            if matrix[i][0] > target:
                r = i - 1
            elif matrix[i][n - 1] < target:
                l = i + 1
            else:
                x = i
                break
        
        
        if x == -1:
            return False

        l = 0
        r = n - 1

        while l <= r:
            
            i = i = l + ((r - l) // 2)

            if matrix[x][i] > target:
                r = i - 1
            elif matrix[x][i] < target:
                l = i + 1
            else:
                return True
        
        return False
