import heapq
from collections import Counter, deque

# TC: O(N*M)
class Solution:
    def leastInterval(self, tasks, n: int) -> int:

        time = 0

        maxHeap = Counter(tasks)
        maxHeap = [-n for n in maxHeap.values()]
        heapq.heapify(maxHeap)

        q = deque()

        while maxHeap or q:

            time += 1

            if maxHeap:
                val = 1 + heapq.heappop(maxHeap)

                if val:
                    q.append([val, time+n])

            if q:
                if q[0][-1] == time:
                    heapq.heappush(maxHeap, q.popleft()[0])

        return time
