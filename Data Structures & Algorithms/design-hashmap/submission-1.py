class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        hashed_key = self._hash(key)
        bucket = self.buckets[hashed_key]

        for i, (searched_key, _) in enumerate(bucket):
            if searched_key == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def get(self, key: int) -> int:
        hashed_key = self._hash(key)
        bucket = self.buckets[hashed_key]

        for searched_key, value in bucket:
            if searched_key == key:
                return value
        
        return -1

    def remove(self, key: int) -> None:
        hashed_key = self._hash(key)
        bucket = self.buckets[hashed_key]

        for searched_key, searched_value in bucket:
            if searched_key == key:
                bucket.remove((searched_key, searched_value))

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)