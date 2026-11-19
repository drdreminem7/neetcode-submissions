class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []
        used = [False] * n
        nums.sort()

        def backtrack():
            if len(sol) == n:
                res.append(sol[:])
                return

            for i in range(n):
                if used[i]: continue
                if i + 1 < n and nums[i] == nums[i + 1] and not used[i + 1]: continue

                sol.append(nums[i])
                used[i] = True
                backtrack()
                sol.pop()
                used[i] = False

        backtrack()
        return res