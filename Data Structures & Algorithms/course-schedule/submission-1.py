class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        UNVISITED, VISITING, VISITED = 0, 1, 2
        states = [UNVISITED] * numCourses

        def bfs(i):
            if states[i] == VISITED: return True
            if states[i] == VISITING: return False

            states[i] = VISITING

            for neighbor in graph[i]:
                if not bfs(neighbor):
                    return False
                
            states[i] = VISITED
            return True

        for i in range(numCourses):
            if not bfs(i):
                return False

        return True

