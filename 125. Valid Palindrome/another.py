import re
s = "A man, a plan, a canal: Panama"

s = re.sub(r'[^a-zA-Z0-9]','',s)
s= s.lower()

print(s==s[::-1])