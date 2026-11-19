class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res, max_heap = "", []
        for count, letter in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count:
                heapq.heappush(max_heap, (count, letter))

        while max_heap:
            count, letter = heapq.heappop(max_heap)
            if len(res) > 1 and res[-1] == res[-2] == letter:
                if not max_heap:
                    break
                count2, letter2 = heapq.heappop(max_heap)
                res += letter2
                count2 += 1
                if count2:
                    heapq.heappush(max_heap, (count2, letter2))
            else:
                res += letter
                count += 1
            
            if count:
                heapq.heappush(max_heap, (count, letter))

        return res