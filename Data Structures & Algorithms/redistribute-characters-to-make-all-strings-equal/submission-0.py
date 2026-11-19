class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        seen_letters = [0] * 26
        for word in words:
            for ch in word:
                seen_letters[ord(ch) - ord("a")] += 1

        for i in range(26):
            if seen_letters[i] % n:
                return False

        return True