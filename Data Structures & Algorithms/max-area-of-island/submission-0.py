class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def bfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n: return 0
            if grid[i][j] == 0: return 0

            grid[i][j] = 0

            return 1 + bfs(i + 1, j) + bfs(i - 1, j) + bfs(i, j + 1) + bfs(i, j - 1)

        maxArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = bfs(i, j)
                    print(area)
                    if area > maxArea: maxArea = area
        
        return maxArea