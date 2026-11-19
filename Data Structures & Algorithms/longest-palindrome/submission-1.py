class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen_letters = defaultdict(int)
        for ch in s:
            seen_letters[ch] += 1

        count = 0
        has_odd = False
        for value in seen_letters.values():
            count += value if value & 1 == 0 else value - 1
            if value & 1:
                has_odd = True

        return count + 1 if has_odd else count