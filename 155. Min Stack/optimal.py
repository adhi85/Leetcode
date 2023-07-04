from collections import deque

class MinStack:

    def __init__(self):
        self.q = deque()
        self.min = 2 ** 31

    def push(self, val: int) -> None:
        if self.q:
            if val < self.min:
                x = val
                # Modifying the value to push to stack which will be smaller than the minimum
                val = (2*val) - self.min
                self.min = x
        else:
            self.min = val
            
        self.q.append(val)

    def pop(self) -> None:
        x = self.q.pop()
        
        # If element in stack is lesser than min it is a modified value  so update the minimum value and then return 
        if x < self.min:
            self.min = (2*self.min) - x
            return self.min
        return x

    def top(self) -> int:
        x = self.q[-1]
        
        if x < self.min:
            return self.min
        return self.q[-1]

    def getMin(self) -> int:
        return self.min