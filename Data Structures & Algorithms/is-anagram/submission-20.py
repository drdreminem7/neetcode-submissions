class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letter_counter = [0] * 26
        for i in range(len(s)):
            letter_counter[ord(s[i]) - ord("a")] += 1
            letter_counter[ord(t[i]) - ord("a")] -= 1

        for i in range(26):
            if letter_counter[i]:
                return False

        return True
            