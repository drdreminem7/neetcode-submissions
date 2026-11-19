class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        i = 0

        result = ""
        while i < n and i < m:
            result += word1[i] + word2[i]
            i += 1

        if i < n: result += word1[i:n]
        if i < m: result += word2[i:m]

        return result