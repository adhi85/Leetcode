from itertools import combinations
nums = [1, 2, 3]

hashset = set()

for i in range(len(nums)+1):
    comb = combinations(nums, i)

    for j in list(comb):
        hashset.add(j)

hashset = [list(sublist) for sublist in hashset]

print(hashset)

# TC: O(n*2^n)
# SC: O(2^n)
