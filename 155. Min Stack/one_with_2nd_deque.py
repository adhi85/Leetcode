from collections import deque

# SC: O(2N)
class MinStack:

    def __init__(self):
        self.q = deque()      
        self.min = deque()
        self.min.append(2**31)

    def push(self, val: int) -> None:
        self.q.append(val)
        if self.min and val <= self.min[-1]:
            self.min.append(val)
            
    def pop(self) -> None:
        if self.q[-1] == self.min[-1]:
            self.min.pop()
        return self.q.pop()

    def top(self) -> int:
        return self.q[-1]

    def getMin(self) -> int:
        if len(self.min) == 1:
            return 0
        return self.min[-1]