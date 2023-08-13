s = "ABAB"
k = 2

l = r = 0
count = [0] * 26
ans = 0

while r < len(s):

    count[ord(s[r])-ord("A")] += 1

    length = r-l + 1

    if length - max(count) <=k:
        ans = max(ans,length)
    else:
        count[ord(s[l])-ord("A")] -= 1
        l +=1
    r +=1

print(ans)
