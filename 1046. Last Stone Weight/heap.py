import heapq


class Solution:
    def lastStoneWeight(self, stones):

        stones = [-s for s in stones]

        heapq.heapify(stones)

        while len(stones) > 1:

            maxi = heapq.heappop(stones)
            maxi2 = heapq.heappop(stones)

            if abs(maxi-maxi2) != 0:
                heapq.heappush(stones, maxi-maxi2)

        return -heapq.heappop(stones) if stones else 0
