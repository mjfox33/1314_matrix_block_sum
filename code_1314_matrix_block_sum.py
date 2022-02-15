class Solution:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        n = len(mat)
        m = len(mat[0]) # assuming all rows have the same number of columns
        result = [ [0]*m for _ in range(n)]

        # build prefix_sum matrix
        prefix_sum = [ [0]*m for _ in range(n)]
        for row in range(n):
            for col in range(m):
                prefix_sum[row][col] += mat[row][col]
                if col > 0:
                    prefix_sum[row][col] += prefix_sum[row][col-1]
                if row > 0:
                    prefix_sum[row][col] += prefix_sum[row-1][col]
                if col > 0 and row > 0:
                    prefix_sum[row][col] -= prefix_sum[row-1][col-1]

        # now calculate values for each cell using prefix sum matrix
        for row in range(n):
            for col in range(m):
                result[row][col] = prefix_sum[min(n-1, row+k)][min(m-1, col+k)]
                if row > k:
                    result[row][col] -= prefix_sum[row-k-1][min(m-1, col+k)]
                if col > k:
                    result[row][col] -= prefix_sum[min(n-1, row+k)][col-k-1]
                if row > k and col > k:
                    result[row][col] += prefix_sum[row-k-1][col-k-1] 

        return result