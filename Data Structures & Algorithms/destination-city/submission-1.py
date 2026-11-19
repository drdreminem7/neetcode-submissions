class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        hash_map = {}
        for start, end in paths:
            hash_map[start] = end

        for key, value in hash_map.items():
            if value not in hash_map:
                return value

        return ""
