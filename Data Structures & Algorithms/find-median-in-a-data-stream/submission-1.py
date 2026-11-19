class MedianFinder:

    def __init__(self):
        self.length = 0
        self.left_side_max_heap = []
        self.right_side_min_heap = []

    def addNum(self, num: int) -> None:
        if self.length & 1:
            heapq.heappush(self.right_side_min_heap, num)
        else:
            heapq.heappush(self.left_side_max_heap, -num)
        
        self.length += 1

        if self.right_side_min_heap and self.right_side_min_heap[0] < -self.left_side_max_heap[0]:
            right_min = heapq.heappop(self.right_side_min_heap)
            left_max = -heapq.heappop(self.left_side_max_heap)

            heapq.heappush(self.right_side_min_heap, left_max)
            heapq.heappush(self.left_side_max_heap, -right_min)


    def findMedian(self) -> float:
        if self.length == 0: return None
        if self.length & 1:
            return -self.left_side_max_heap[0]
        else:
            return (-self.left_side_max_heap[0] + self.right_side_min_heap[0]) / 2


        