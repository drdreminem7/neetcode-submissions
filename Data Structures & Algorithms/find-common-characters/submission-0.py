class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counter = Counter(words[0])
        n = len(words)

        for i in range(1, n):
            current_counter = Counter(words[i])
            for ch in counter:
                counter[ch] = min(counter[ch], current_counter[ch])

        result = []
        for ch in counter:
            for i in range(counter[ch]):
                result.append(ch)

        return result