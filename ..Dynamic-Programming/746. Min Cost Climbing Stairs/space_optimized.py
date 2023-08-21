cost = [10,15,20]

prev2 = cost[0]
prev1 = cost[1]

for i in range(2,len(cost)):
    new = cost[i] + min(prev1,prev2)
    prev2 = prev1
    prev1 = new

print(min(prev1,prev2))

# TC: O(N)
# SC: O(1)