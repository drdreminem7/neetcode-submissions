class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        d = self.trie
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d['/'] = '/'

    def search(self, word: str) -> bool:
        def dfs(d, index):
            if index == len(word): return '/' in d

            if word[index] != '.':
                if word[index] not in d:
                    return False
                else:
                    return dfs(d[word[index]], index + 1)
            else:
                return any(dfs(d[letter], index + 1) for letter in d if letter != '/')

        return dfs(self.trie, 0)

                    
