class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        curr_passengers, min_heap = 0, []

        for passengers, start, end in trips:
            while min_heap and min_heap[0][0] <= start:
                curr_passengers -= min_heap[0][1]
                heapq.heappop(min_heap)
            
            curr_passengers += passengers
            if curr_passengers > capacity: return False

            heapq.heappush(min_heap, (end, passengers))

        return True
            
