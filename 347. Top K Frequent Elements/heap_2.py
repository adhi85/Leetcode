import heapq

nums = [1, 1, 1, 2, 2, 3]

k = 2

hashmap = {}

for i in nums:
    hashmap[i] = 1 + hashmap.get(i, 0)

nums = [(-v, k) for k, v in hashmap.items()]

heapq.heapify(nums)
ans = []

for i in range(k):
    ans.append(heapq.heappop(nums)[1])
print(ans)
