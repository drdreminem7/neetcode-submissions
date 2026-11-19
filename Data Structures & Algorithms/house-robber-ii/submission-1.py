class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        dp = [[-1] * 2 for _ in range(n)]

        def dfs(i, flag):
            if i >= n or (flag and i == len(nums) - 1):
                return 0

            if dp[i][flag] != -1:
                return dp[i][flag]
            else:
                dp[i][flag] = max(dfs(i + 1, flag), nums[i] + dfs(i + 2, flag or i == 0))
                return dp[i][flag]

        return max(dfs(0, True), dfs(1, False))
           