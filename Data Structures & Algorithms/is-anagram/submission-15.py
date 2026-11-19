class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seenLetters = [0] * 26
        for letter in s: seenLetters[ord(letter) - ord("a")] += 1
        for letter in t: seenLetters[ord(letter) - ord("a")] -= 1
        for i in range(26):
            if seenLetters[i] != 0: return False
        return True