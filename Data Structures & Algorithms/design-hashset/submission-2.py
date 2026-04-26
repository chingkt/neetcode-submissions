class MyHashSet:

    def __init__(self):
        self.size = 10
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        bucket = self.buckets[key % self.size]
        if self.contains(key):
            return None
        bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self.buckets[key % self.size]
        if self.contains(key):
            self.buckets[key % self.size].remove(key)

    def contains(self, key: int) -> bool:
        bucket = self.buckets[key % self.size]
        for elem in bucket:
            if elem == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)