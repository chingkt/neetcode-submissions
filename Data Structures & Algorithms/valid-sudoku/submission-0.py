class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSets = [set() for _ in range(9)]
        colSets = [set() for _ in range(9)]
        boxSets = [set() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                value = board[i][j]
                boxNum = self.getBoxNumber(i, j)
                if value == ".":
                    continue
                elif value in rowSets[i] or value in colSets[j] or value in boxSets[boxNum]:
                    print(value)
                    print(value in rowSets[i], value in colSets[j], value in boxSets[boxNum])
                    return False
                else:
                    rowSets[i].add(value)
                    colSets[j].add(value)
                    boxSets[boxNum].add(value)
        return True

    def getBoxNumber(self, row: int, col: int) -> int:
        if row <= 2:
            if col <= 2:
                return 0
            elif col <= 5:
                return 1
            elif col <= 8:
                return 2
        elif row <= 5:
            if col <= 2:
                return 3
            elif col <= 5:
                return 4
            elif col <= 8:
                return 5
        else:
            if col <= 2:
                return 6
            elif col <= 5:
                return 7
            elif col <= 8:
                return 8
        return 9
                