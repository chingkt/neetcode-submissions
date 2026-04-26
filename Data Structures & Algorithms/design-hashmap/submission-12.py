class MyNode:
    def __init__(self, key: int | None, value: int | None):
        self.key = key
        self.value = value
        self.next = None

    def add_next(self, key, value) -> None:
        self.next = MyNode(key, value)


class MyHashMap:

    def __init__(self):
        self.size = 10
        self.buckets = [MyNode(None, None) for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        ind = key % self.size
        
        current_node = self.buckets[ind]
        while True:
            if current_node.key == None:
                current_node.key = key
                current_node.value = value
                break
            elif key == current_node.key:
                current_node.value = value
                break
            elif current_node.next == None:
                current_node.next = MyNode(key, value)
                break
            else:
                current_node = current_node.next
        



    def get(self, key: int) -> int:
        ind = key % self.size

        current_node = self.buckets[ind]
        if current_node.key == key and current_node.value != None:
            return current_node.value
        
        while current_node.next:
            current_node = current_node.next
            if current_node.key != None and current_node.value != None:
                return current_node.value
        return -1




    def remove(self, key: int) -> None:
        ind = key % self.size
        previous_node = current_node = self.buckets[ind]

        removed = False
        while not removed and current_node:
            if current_node.key == key:
                if not current_node.next:
                    current_node.key = None
                    current_node.value = None
                    removed = True
                else:
                    next_node = current_node.next
                    current_node.key = next_node.key
                    current_node.value = next_node.value
                    current_node.next = next_node.next
                    removed = True
            else:
                current_node = current_node.next



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)