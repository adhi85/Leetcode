class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []

        # remove k digits
        for digit in num:
            # if stack is not empty and the last element in stack is greater than the current digit
            # pop the last element in stack and decrement k by 1
            while k > 0 and stack and stack[-1] > digit:
                k -= 1
                stack.pop()
            stack.append(digit)

        res = "".join(stack)
        # if k is not 0, remove the last k elements in stack to make the length of stack to be len(stack)-k
        res = res[:len(stack)-k]

        # res = str(int(res))
        res = res.lstrip("0") # remove leading zeros

        return res if res else "0"
    
T = Solution()
print(T.removeKdigits("1432219", 3)) # "1219"
