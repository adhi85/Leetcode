s = "anagram"
t = "nagaram"
ct = {}
ct2 = {}

if len(t) != len(s):
    print("False")
else:
    for i in range(len(s)):
        ct[s[i]] = s.count(s[i])
        ct2[t[i]] = t.count(t[i])            
    
    print(ct == ct2)