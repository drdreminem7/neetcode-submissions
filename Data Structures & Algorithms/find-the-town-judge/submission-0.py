class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        hash_map = defaultdict(int)
        for a, b in trust:
            hash_map[a] -= 1
            hash_map[b] += 1

        for i in range(1, n + 1):
            if hash_map[i] == n - 1:
                return i

        return -1