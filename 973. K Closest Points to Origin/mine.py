import heapq


class Solution:
    def kClosest(self, points, k):

        for i in points:
            d = i[0]**2 + i[1]**2
            i.insert(0, d)

        heapq.heapify(points)

        ans = []

        while k:
            x = heapq.heappop(points)
            ans.append([x[1], x[2]])
            k -= 1

        return ans
