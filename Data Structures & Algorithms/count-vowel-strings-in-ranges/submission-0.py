class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeoiu")
        def isStartingEndingWithVowels(word):
            return word[0] in vowels and word[-1] in vowels

        n, words[0] = len(words), 1 if words[0] and isStartingEndingWithVowels(words[0]) else 0
        for i in range(1, n):
            words[i] = words[i - 1] + (1 if isStartingEndingWithVowels(words[i]) else 0)

        print(words)
        
        res = []
        for query in queries:
            if query[0] == 0: 
                res.append(words[query[1]])
                continue
            res.append(words[query[1]] - words[query[0] - 1])

        return res
            
