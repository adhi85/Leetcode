from itertools import permutations

class Solution:
    def generateParenthesis(self, n: int):
        
        def isValid(s):
            stack = []
            for i in s:
                if i == '(':    
                    stack.append(i)
                else:
                    try:
                        stack.pop()
                        
                    except:
                        return -1
            if len(stack):
                return -1
            return 1
                
        
        al = [''.join(w) for w in permutations('()'*n)]
        ans = []
        
        for i in al:
            stack = []
            
            x = isValid(i)
            
            if x ==1:
                ans.append(i)
        return list(set(ans))
                