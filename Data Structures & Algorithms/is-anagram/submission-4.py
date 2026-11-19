class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occurrences = [0] * 26
        for letter in s: occurrences[ord(letter) - ord('a')] += 1
        for letter in t: occurrences[ord(letter) - ord('a')] -= 1
        for num in occurrences:
            if num != 0: return False

        return True