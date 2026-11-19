class Solution:        
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        perimeter = 0

        def bfs(i, j):
            nonlocal perimeter
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                perimeter += 1
                return

            if grid[i][j] == 2: 
                return

            grid[i][j] = 2
            
            for i_off, j_off in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                bfs(i + i_off, j + j_off)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs(i, j)
                    return perimeter

        return 0
    

    