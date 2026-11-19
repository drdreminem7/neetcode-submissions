class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        max_heap = [[-cnt, letter] for letter, cnt in counter.items()]
        heapq.heapify(max_heap)
        
        res = ""
        prev = None

        while max_heap or prev:
            if prev and not max_heap: 
                return ""

            cnt, letter = heapq.heappop(max_heap)
            res += letter
            cnt += 1

            if prev:
                heapq.heappush(max_heap, prev)
                prev = None

            if cnt != 0:
                prev = [cnt, letter]

        return res



        