class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = Counter(chars)
        sum = 0
        for word in words:
            temp_counter = counter.copy()
            valid = True
            for ch in word:
                if ch not in temp_counter:
                    valid = False
                    break
                temp_counter[ch] -= 1
                if temp_counter[ch] < 0:
                    valid = False
                    break

            if valid:
                sum += len(word)

        return sum

