class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        longest = 0
        curr = 0
        for i in range(len(s)):
            if s[i] in seen and curr >= i - seen[s[i]]: curr = i - seen[s[i]]
            else: curr += 1

            seen[s[i]] = i
            longest = max(longest, curr)
        return longest