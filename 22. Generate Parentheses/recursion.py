# Only add open paranthesis if open < n
# Only add closed paranthesis if closed < open
# It is a valif IFF closed == open == n

class Solution:
    def generateParenthesis(self, n: int):
        
        stack = []
        ans = []
        
        def backTrack(openN, closedN):
            
            if openN == closedN == n:
                ans.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backTrack(openN+1,closedN)
                stack.pop()
                
            if closedN < openN:
                stack.append(")")
                backTrack(openN,closedN+1)
                stack.pop()
                
        
        backTrack(0,0)
        return ans