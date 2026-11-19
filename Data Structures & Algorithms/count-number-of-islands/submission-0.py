class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def bfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n: return
            if grid[i][j] == "0": return

            grid[i][j] = "0"

            for i_off, j_off in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                bfs(i + i_off, j + j_off)

        islands = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands += 1
                    bfs(i, j)

        return islands