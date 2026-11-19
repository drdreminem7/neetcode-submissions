class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2: return min(cost)
        
        dp = [-1] * (len(cost) + 1)

        def dfs(i):
            if i >= len(cost):
                return 0

            if dp[i] != -1:
                return dp[i]
            else:
                dp[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
                return dp[i]

        return min(dfs(0), dfs(1))
