class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        seenLetters = [0] * 26
        for ch in text:
            seenLetters[ord(ch) - ord("a")] += 1

        min_count = float("inf")
        for ch in "balon":
            count = seenLetters[ord(ch) - ord("a")]
            if ch == "l" or ch == "o":
                count //= 2
            min_count = min(min_count, count)
        return min_count
                
