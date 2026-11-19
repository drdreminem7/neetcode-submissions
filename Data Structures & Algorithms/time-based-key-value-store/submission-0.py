class TimeMap:
    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append((timestamp, value))
        else:
            self.map[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map: return ""
        stamps = self.map[key]
        if timestamp < stamps[0][0]: return ""

        n = len(stamps)
        start, end = 0, n - 1
        while start <= end:
            mid = start + (end - start) // 2
            if stamps[mid][0] > timestamp: end = mid - 1
            else: start = mid + 1

        return stamps[start - 1][1]
            
