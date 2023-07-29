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
            for i in reversed(self.hash[key]):
                if i[1] <= timestamp:
                    return i[0]
            return ""
