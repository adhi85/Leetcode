from collections import deque

# SC: O(2N)
class MinStack:

    def __init__(self):
        self.q = deque()

    def push(self, val: int) -> None:
        if self.q :
            self.q.append((val,min(self.q[-1][1],val)))
        else:
            self.q.append((val,val))

    def pop(self) -> None:
        x = self.q.pop()
        return x[0]

    def top(self) -> int:
        return self.q[-1][0]

    def getMin(self) -> int:
        return self.q[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()