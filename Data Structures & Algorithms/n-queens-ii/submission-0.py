class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0

        used_cols = set()
        used_pos_diag = set()
        used_neg_diag = set()

        queens_col_indices = []

        def backtrack(row):
            nonlocal res
            if row == n:
                res += 1
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
