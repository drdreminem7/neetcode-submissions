class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        stack = deque()

        for i in range(n):
            if board[0][i] == "O": stack.append((0, i))
            if m > 1 and board[m - 1][i] == "O": stack.append((m - 1, i))
        
        for i in range(1, m - 1):
            if board[i][0] == "O": stack.append((i, 0))
            if n > 1 and board[i][n - 1] == "O": stack.append((i, n - 1))

        while stack:
            i, j = stack.pop()
            board[i][j] = "S"
            for i_off, j_off in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                r, c = i + i_off, j + j_off
                if 0 <= r < m and 0 <= c < n and board[r][c] == "O":
                    stack.append((r, c))

        for i in range(m):
            for j in range(n):
                if board[i][j] == "S":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
