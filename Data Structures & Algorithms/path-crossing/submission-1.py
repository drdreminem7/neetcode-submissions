class Solution:
    def isPathCrossing(self, path: str) -> bool:
        start = (0, 0)
        hash_set = {start}
        points = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}
        for direction in path:
            start = tuple(x + y for x,y in zip(start, points[direction]))
            print(start)
            if start in hash_set:
                return True
            hash_set.add(start)

        return False