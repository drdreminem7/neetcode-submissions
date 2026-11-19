import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = sys.maxsize
        profit = 0
        for num in prices:
            if curr < num: profit += num - curr
            curr = num

        return profit
