class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m * n - 1

        while l <= r:

            i = l + ((r - l) // 2)

            row = i // n
            col = i % n
            val = matrix[row][col]

            print(row, col, val)

            if val > target:
                r = i - 1
            elif val < target:
                l = i + 1
            else:
                return True

        return False