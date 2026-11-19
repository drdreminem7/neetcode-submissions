class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start, end = max(weights), sum(weights)
        res = end
        while start <= end:
            cap = (start + end) // 2
            currCap = 0
            runningDays = 1
            for weight in weights: 
                if currCap + weight > cap:
                    currCap = weight
                    runningDays += 1
                else: currCap += weight
            
            if runningDays <= days:
                res = min(res, cap)
                end = cap - 1
            else: start = cap + 1

        return res