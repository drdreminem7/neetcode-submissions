"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        def make(row_top, row_bottom, col_left, col_right):
            first_val = grid[row_top][col_left]
            for i in range(row_top, row_bottom + 1):
                for j in range(col_left, col_right + 1):
                    if grid[i][j] != first_val:
                        mid_row = row_top + (row_bottom - row_top) // 2
                        mid_col = col_left + (col_right - col_left) // 2

                        top_left = make(row_top, mid_row, col_left, mid_col)
                        top_right = make(row_top, mid_row, mid_col + 1, col_right)
                        bottom_left = make(mid_row + 1, row_bottom, col_left, mid_col)
                        bottom_right = make(mid_row + 1, row_bottom, mid_col + 1, col_right)

                        return Node(1, False, top_left, top_right, bottom_left, bottom_right)

            return Node(int(first_val == 1), True, None, None, None, None)


        return make(0, n - 1, 0, n - 1)
