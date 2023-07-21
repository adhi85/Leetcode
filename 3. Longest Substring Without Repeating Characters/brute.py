s = "abcabcbb"

if len(s)==0 or len(s) ==1:
    print(len(s))

l,r = 0,1
ans = 1

count = 1
while r < len(s):
    if s[r] not in s[l:r]:
        count +=1
        r +=1
        ans = max(count,ans)
    else:
        l += 1
        r = l+1
        count = 1
print(ans)