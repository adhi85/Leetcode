prices = [7,1,5,3,6,4]

pro = 0

for i in range(len(prices)-1):
    for j in range(i, len(prices)):
        k = prices[j] - prices[i]
        if(k > pro):
            pro = k

# TC : O(n^2)
print(pro)
    
