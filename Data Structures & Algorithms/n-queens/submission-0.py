class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        used_cols = set()
        used_pos_diag = set()
        used_neg_diag = set()

        queens_col_indices = []

        def backtrack(row):
            if row == n:
                board = []
                for c in queens_col_indices:
                    dots_before = '.' * c
                    dots_after = '.' * (n - c - 1)
                    row_string = dots_before + 'Q' + dots_after
                    board.append(row_string)
                res.append(board)
                return

            for col in range(n):
                if col in used_cols or (row+col) in used_pos_diag or (row-col) in used_neg_diag:
                    continue

                queens_col_indices.append(col)
                used_cols.add(col)
                used_pos_diag.add(row+col)
                used_neg_diag.add(row-col)

                backtrack(row + 1)

                queens_col_indices.pop()
                used_cols.remove(col)
                used_pos_diag.remove(row+col)
                used_neg_diag.remove(row-col)
            
        backtrack(0)
        return res

