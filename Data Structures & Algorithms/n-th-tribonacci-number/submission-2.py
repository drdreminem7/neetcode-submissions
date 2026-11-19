class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        dp = [-1] * (n + 1)
        dp[0] = 0
        dp[1] = dp[2] = 1

        def f(x):
            if dp[x] != -1:
                return dp[x]
            else:
                dp[x] = f(x - 1) + f(x - 2) + f(x - 3)
                return dp[x]

        return f(n)