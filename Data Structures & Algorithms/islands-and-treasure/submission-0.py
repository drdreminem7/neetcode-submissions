class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        INF = 2147483647
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


        while queue:
            i, j = queue.popleft()

            for i_off, j_off in directions:
                r, c = i + i_off, j + j_off

                if 0 <= r < m and 0 <= c < n:
                    if grid[r][c] == INF:
                        grid[r][c] = grid[i][j] + 1
                        queue.append((r,c))

            
            

        