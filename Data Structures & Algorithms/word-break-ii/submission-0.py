class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res, sol = [], []
        n = len(s)

        def backtrack(i):
            if i == n:
                res.append(" ".join(sol))
                return

            for j in range(i, n):
                word = s[i:j+1]
                if word in wordDict:
                    sol.append(word)
                    backtrack(j + 1)
                    sol.pop()

        backtrack(0)
        return res