import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minDay, maxProfit = 101, 0
        for i in range(len(prices)):
            if minDay > prices[i]: minDay = prices[i]
            maxProfit = max(maxProfit, prices[i] - minDay)
        return maxProfit