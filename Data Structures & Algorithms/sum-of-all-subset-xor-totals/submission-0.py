class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        res, sol = 0, 0

        def backtrack(i):
            nonlocal res, sol
            if i == n:
                res += sol
                return

            backtrack(i + 1)
            sol ^= nums[i]
            backtrack(i + 1)
            sol ^= nums[i]

        backtrack(0)
        return res