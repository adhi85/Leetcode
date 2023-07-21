height = [1,8,6,2,5,4,8,3,7]
i = 0
j = len(height)-1
maxa = 0

while i < j:
    x = min(height[i], height[j])
    
    if x == height[i]:
        area = (j-i) * x
        i +=1
    elif x == height[j]:
        area = (j-i) * x
        j -=1
    maxa = max(area,maxa)

print(maxa)