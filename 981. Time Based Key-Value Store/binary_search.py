from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.hash = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.hash:
            return ""

        else:

            l, r = 0, len(self.hash[key])-1
            ans = ""

            while l <= r:
                m = (l+r) >> 1

                if self.hash[key][m][1] <= timestamp:

                    ans = self.hash[key][m][0]
                    l = m+1

                else:
                    r = m-1

            return ans
