class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_rows = []
        zero_cols = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_rows.append(i)
                    zero_cols.append(j)
        for i in zero_rows:
            for k in range(len(matrix[0])):
                matrix[i][k] = 0
        for j in zero_cols:
            for m in range(len(matrix)):
                matrix[m][j] = 0

        return matrix
