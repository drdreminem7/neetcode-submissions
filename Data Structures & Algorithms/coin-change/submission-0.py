class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = { 0 : 0 }

        def min_coins(amt):
            if amt in dp:
                return dp[amt]
            
            minn = float("inf")
            for coin in coins:
                diff = amt - coin
                if diff < 0:
                    break
                minn = min(minn, 1 + min_coins(diff))
            
            dp[amt] = minn
            return minn

        result = min_coins(amount)
        return result if result != float("inf") else -1