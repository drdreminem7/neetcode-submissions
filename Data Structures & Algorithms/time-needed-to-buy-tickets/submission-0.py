class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        seconds, index = 0, 0
        res = 0
        for i in range(len(tickets)):
            if i <= k:
                res += min(tickets[i], tickets[k])
            else:
                res += min(tickets[i], tickets[k] - 1)

        return res
        