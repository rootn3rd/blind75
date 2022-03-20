class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next, self.prev = None, None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def add(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    # left : LRU and right : most recent
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])  # remove from middle
            self.add(self.cache[key])  # add to right
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.add(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]  # delete from cache

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


lRUCache = LRUCache(2)
lRUCache.put(1, 1)  # // cache is {1=1}
lRUCache.put(2, 2)  # // cache is {1=1, 2=2}
lRUCache.get(1)  # // return 1
lRUCache.put(3, 3)  # // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2)  # // returns -1 (not found)
lRUCache.put(4, 4)  # // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1)  # // return -1 (not found)
lRUCache.get(3)  # // return 3
lRUCache.get(4)  # // return 4
