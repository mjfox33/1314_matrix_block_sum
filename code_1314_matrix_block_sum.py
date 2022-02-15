class Solution:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        n = len(mat)
        m = len(mat[0]) # assuming all rows have the same number of columns
        result = [ [0]*m for _ in range(n)]
        for row in range(n):
            for col in range(m):
                for row_delta in range(-k, k+1, 1):
                    for col_delta in range(-k, k+1, 1):
                        row_index = row + row_delta
                        col_index = col + col_delta
                        if  row_index < 0 or row_index > n-1 or col_index < 0 or col_index > m-1:
                            continue
                        result[row][col] += mat[row+row_delta][col+col_delta]
        return result