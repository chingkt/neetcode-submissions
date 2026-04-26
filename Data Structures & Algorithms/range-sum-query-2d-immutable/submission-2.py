class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sum_matrix = self.build_sum_matrix(matrix)

    def build_sum_matrix(self, matrix: List[List[int]]):
        sum_matrix = [[-math.inf for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j == 0:
                    sum_matrix[i][j] = matrix[i][j]
                else:
                    sum_matrix[i][j] = sum_matrix[i][j-1] + matrix[i][j]
        return sum_matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        sum_matrix = self.sum_matrix
        for i in range(row1, row2+1, 1):
            if col1 - 1 > -1:
                res += sum_matrix[i][col2] - sum_matrix[i][col1 - 1]
            else:
                res += sum_matrix[i][col2]
        return res



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)