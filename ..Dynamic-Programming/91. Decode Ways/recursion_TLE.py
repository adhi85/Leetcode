class Solution:
    def numDecodings(self, s):

        def decode(i):

            # If indx goes out by one => reach last step one by one
            if i == len(s):
                return 1

            # If there is "0" that branch becomes invalid 
            if s[i] == "0":
                return 0
            
            """ 
            we are Going as dfs to the last element
            and then  checking two letters from backside.
            i depends on i+1 and i +2

            """
            ans = decode(i+1)

            # Checking if i is second last index and also if the two digit n.o is valid(b/w 0 and 26)
            if i + 1 < len(s) and 0 < int(s[i:i+2]) < 27:
                ans += decode(i+2)

            return ans
        
        return decode(0)
        
T = Solution()

s = "226"
print(T.numDecodings(s))
            
