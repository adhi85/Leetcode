class Solution:
    def fib(self, n: int) -> int:

        prev2 = 0
        prev1 = 1
        if n == 0:
            return 0
        for i in range(2, n+1):
            curr = prev2 + prev1
            prev2, prev1 = prev1, curr

        return prev1

