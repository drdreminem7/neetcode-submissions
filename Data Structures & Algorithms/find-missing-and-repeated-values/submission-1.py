class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        n = len(grid)
        res = [0] * 2
        for i in range(n * n):
            num = grid[i // n][i % n]
            if num not in seen:
                seen.add(num)
            else:
                res[0] = num

        for i in range(1, n * n + 1):
            if i not in seen:
                res[1] = i
            
        return res
