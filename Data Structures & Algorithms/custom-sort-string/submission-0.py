class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hash_set = set(order)
        hash_map = defaultdict(int)
        for ch in s:
            hash_map[ch] += 1

        res = ""
        for ch in order:
            if ch in hash_map:
                res += (ch * hash_map[ch])
                hash_map.pop(ch)

        for key, value in hash_map.items():
            res += (key * value)

        return res
