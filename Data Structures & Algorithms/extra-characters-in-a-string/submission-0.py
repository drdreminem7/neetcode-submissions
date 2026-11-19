class Solution:
    class Trie:
        def __init__(self):
            self.trie = {}

        def add_word(self, word: str):
            curr = self.trie
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['.'] = '.'

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = self.Trie()
        for word in dictionary:
            trie.add_word(word)

        dp = {len(s) : 0}

        def dfs(i):
            if i in dp: return dp[i]

            res = 1 + dfs(i + 1)
            curr = trie.trie
            for j in range(i, len(s)):
                if s[j] not in curr: break
                curr = curr[s[j]]
                if '.' in curr:
                    res = min(res, dfs(j + 1))

            dp[i] = res
            return res

        return dfs(0)
        