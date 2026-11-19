class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_queue = deque()
        p_seen = set()

        a_queue = deque()
        a_seen = set()

        m, n = len(heights), len(heights[0])

        for i in range(n):
            p_queue.append((0, i))
            p_seen.add((0, i))

        for j in range(1, m):
            p_queue.append((j, 0))
            p_seen.add((j, 0))

        for i in range(n):
            a_queue.append((m - 1, i))
            a_seen.add((m - 1, i))

        for j in range(0, m - 1):
            a_queue.append((j, n - 1))
            a_seen.add((j, n - 1))

        def get_coords(queue, seen):
            coords = set()
            while queue:
                i, j = queue.popleft()
                coords.add((i, j))
                for i_off, j_off in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    r, c = i + i_off, j + j_off
                    if 0 <= r < m and 0 <= c < n and heights[r][c] >= heights[i][j] and  (r, c) not in seen:
                        queue.append((r, c))
                        seen.add((r, c))

            return coords

        p_coords = get_coords(p_queue, p_seen)
        a_coords = get_coords(a_queue, a_seen)

        return list(p_coords.intersection(a_coords))






