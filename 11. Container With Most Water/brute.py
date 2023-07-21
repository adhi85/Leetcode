height = [1,8,6,2,5,4,8,3,7]

maxa = 0

for i in range(len(height)-1):
    for j in range(i+1,len(height)):
        x = min(height[i],height[j])
        
        area = abs(j-i) * x
        
        maxa = max(maxa,area)
print(maxa)