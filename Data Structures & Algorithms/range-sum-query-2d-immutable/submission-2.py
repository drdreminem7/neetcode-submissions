class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefixMatrix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for i in range(rows):
            prefix = 0
            for j in range(cols):
                prefix += matrix[i][j]
                above = self.prefixMatrix[i][j + 1]
                self.prefixMatrix[i + 1][j + 1] = prefix + above

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        r1, c1, r2, c2 = r1 + 1, c1 + 1, r2 + 1, c2 + 1
        bottomRight = self.prefixMatrix[r2][c2]
        above = self.prefixMatrix[r1 - 1][c2]
        left = self.prefixMatrix[r2][c1 - 1]
        topLeft = self.prefixMatrix[r1 - 1][c1 - 1]

        return bottomRight - left - above + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)