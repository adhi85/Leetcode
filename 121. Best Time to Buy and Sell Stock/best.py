prices = [7,6,4,3,1]
minp = prices[0]
maxp = 0

for i in range(len(prices)):
    if(prices[i]<minp):
        minp = prices[i]
    if prices[i]-minp > maxp :
        maxp = prices[i]- minp

# TC: O(n)
# SC: O(1)
print(maxp)