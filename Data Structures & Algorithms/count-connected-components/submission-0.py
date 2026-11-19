class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        components = 0
        seen = set()

        def dfs(node, seen):
            if node in seen: return False
            seen.add(node)
            for neighbor in graph[node]:
                dfs(neighbor, seen)
            return True

        for i in range(n):
            if dfs(i, seen):
                components += 1

        return components