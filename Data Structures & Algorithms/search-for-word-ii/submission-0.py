class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            curr = trie
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['.'] = word
        
        m, n = len(board), len(board[0])
        return_words = []

        def backtrack(i, j, parent):
            letter = board[i][j]
            curr = parent[letter]

            if '.' in curr: 
                return_words.append(curr.pop('.'))

            board[i][j] = '#'

            for i_off, j_off in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                r, c = i + i_off, j + j_off
                if 0 <= r < m and 0 <= c < n and board[r][c] in curr:
                    backtrack(r, c, curr)

            board[i][j] = letter

            if not curr: parent.pop(letter)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    backtrack(i, j, trie)

        return return_words




