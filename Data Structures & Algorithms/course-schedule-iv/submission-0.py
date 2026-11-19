class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        def dfs(node, target, seen):
            if node == target: return True
            if node in seen: return False

            seen.add(node)

            for neighbor in graph[node]:
                if dfs(neighbor, target, seen):
                    return True

            return False

        solution = []
        for a, b in queries:
            seen = set()
            solution.append(a != b and dfs(a, b, seen))

        return solution