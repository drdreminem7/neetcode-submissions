class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        occurrences = defaultdict(list)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.': continue

                for pair in occurrences[board[i][j]]:
                    if pair[0] == i: return False
                    if pair[1] == j: return False
                    if pair[0] // 3 == i // 3 and pair[1] // 3 == j // 3: return False

                occurrences[board[i][j]].append((i, j))

        return True
