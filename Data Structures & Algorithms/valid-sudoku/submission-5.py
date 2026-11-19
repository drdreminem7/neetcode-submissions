class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".": continue
                val = int(board[i][j]) - 1
                mask = 1 << val

                if mask & rows[i]: return False
                if mask & cols[j]: return False
                if mask & squares[(i // 3) * 3 + (j // 3)]: return False

                rows[i] |= mask
                cols[j] |= mask
                squares[(i // 3) * 3 + (j // 3)] |= mask

        return True
