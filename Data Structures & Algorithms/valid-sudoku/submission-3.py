class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        occurrences = defaultdict(list)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue

                for pair in occurrences[board[i][j]]:
                    if pair[0] == i or pair[1] == j or (pair[0] // 3 == i // 3 and pair[1] // 3 == j // 3): return False

                occurrences[board[i][j]].append((i, j))

        return True
