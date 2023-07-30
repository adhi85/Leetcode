class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hash = {}
        self.left = self.right = Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:

        if key in self.hash:
            self.remove(self.hash[key])
            self.insert(self.hash[key])

            return self.hash[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.remove(self.hash[key])

        new = Node(key, value)
        self.insert(new)
        self.hash[key] = new

        if len(self.hash) > self.cap:
            del self.hash[self.left.next.key]
            self.remove(self.left.next)
