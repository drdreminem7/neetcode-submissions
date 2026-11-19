class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            subArrays = 0
            currSum = 0
            for n in nums:
                currSum += n
                if currSum > largest:
                    subArrays += 1
                    currSum = n

            return subArrays + 1 <= k

        start, end = max(nums), sum(nums)
        res = end
        while start <= end:
            mid = start + (end - start) // 2
            if canSplit(mid):
                res = mid
                end = mid - 1
            else: 
                start = mid + 1

        return res