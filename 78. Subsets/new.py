nums = [1, 2, 3]

ans = [[]]

for i in nums:
    ans += [sublist + [i] for sublist in ans]

print(ans)

# TC: O(n*2^n)
# SC: O(1)