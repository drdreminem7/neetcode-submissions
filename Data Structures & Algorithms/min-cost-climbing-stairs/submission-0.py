class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2: return min(cost)
        
        dp = [-1] * (len(cost) + 1)
        dp[0] = cost[0]
        dp[1] = cost[1]

        def dfs(i):
            if dp[i] != -1:
                return dp[i]
            else:
                if i == len(cost):
                    dp[i] = min(dfs(i - 1), dfs(i - 2))
                else:
                    dp[i] = cost[i] + min(dfs(i - 1), dfs(i - 2))
                return dp[i]

        return dfs(len(cost))
