class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        num_fresh = 0
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    num_fresh += 1
            
        if num_fresh == 0:
            return 0

        num_minutes = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            q_size = len(queue)
            num_minutes += 1
            
            for _ in range(q_size):
                i, j = queue.popleft()
                for i_off, j_off in directions:
                    r, c = i + i_off, j + j_off
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                        num_fresh -= 1
                        grid[r][c] = 2
                        queue.append((r, c))

                if num_fresh == 0:
                    return num_minutes

        return num_minutes if num_fresh == 0 else -1


            



