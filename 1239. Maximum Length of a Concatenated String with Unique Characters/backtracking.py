class Solution:
    def maxLength(self, arr) -> int:

        counter = set()

        # check if there is any common character between the string and the counter
        def common(counter,s):

            prev = set()
            for c in s:
                if c in counter or c in prev:
                    return True
                prev.add(c)

            return False
        
        # backtrack function to find the maximum length of the string
        def backtrack(index):
            # base case when we reach the end of the array
            if index == len(arr):
                # return the length of the counter set which contains the unique characters of the string
                return len(counter)
            
            # If the string has no common characters with the counter set, then add the characters of the string to the counter set
            res = 0
            if not common(counter,arr[index]):

                # add the characters of the string to the counter set
                for c in arr[index]:
                    counter.add(c)

                # find the maximum length of the string by calling the backtrack function recursively with the next index
                res = backtrack(index+1)

                # remove the characters of the string from the counter set
                for c in arr[index]:
                    counter.remove(c)

            # find the maximum length of the string by calling the backtrack function recursively with the next index
            return max(res,backtrack(index+1))