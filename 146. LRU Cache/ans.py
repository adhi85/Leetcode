class Node:
    def __init__(self, k=0, v=0):
        self.key = k
        self.val = v
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = dict()
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.data:
            new = Node(key, self.data[key].val)
            x = self.data[key].val

            temp = self.data[key].prev

            self.remove(temp)

            self.add(new)

            self.data[key] = new
            return x
        return -1

    def add(self, new):
        new.next = self.head.next
        self.head.next = new
        new.next.prev = new
        new.prev = self.head

    def remove(self, temp):
        temp.next = temp.next.next
        temp.next.prev = temp

    def put(self, key: int, value: int) -> None:
        if (key not in self.data):
            if len(self.data) < self.capacity:
                new = Node(key, value)
                self.add(new)
                self.data[key] = new
            else:
                x = self.tail.prev
                del self.data[x.key]

                x.prev.next = self.tail
                self.tail.prev = x.prev

                new = Node(key, value)
                self.add(new)
                self.data[key] = new
        else:
            temp = self.data[key].prev
            self.remove(temp)
            new = Node(key, value)
            self.add(new)
            self.data[key] = new


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
