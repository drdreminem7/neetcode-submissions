class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res, sol = [], []

        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        def backtrack(i):
            if i >= n:
                res.append(sol[:])
                return

            for j in range(i, n):
                if isPalindrome(i, j):
                    sol.append(s[i: j + 1])
                    backtrack(j + 1)
                    sol.pop()

        backtrack(0)
        return res