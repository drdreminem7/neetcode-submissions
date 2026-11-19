class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        start = 0
        counts = [0] * 26

        for end in range(len(s)):
            counts[ord(s[end]) - ord("A")] += 1
            while (end - start + 1) - max(counts) > k:
                counts[ord(s[start]) - ord("A")] -= 1
                start += 1
            longest = max(longest, end - start + 1)
        
        return longest