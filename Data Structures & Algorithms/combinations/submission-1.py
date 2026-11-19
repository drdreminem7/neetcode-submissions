class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, sol = [], []
        
        def backtrack(i):
            if len(sol) == k:
                res.append(sol[:])
                return

            if i == n: 
                return

            backtrack(i + 1)
            sol.append(i + 1)
            backtrack(i + 1)
            sol.pop()

        backtrack(0)

        return res