class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        n = len(words)
        if n == 1:
            return words[0][0] == words[0][-1]

        for i in range(1, n + 1):
            if words[i % n][0] != words[i - 1][-1]:
                return False

        return True
