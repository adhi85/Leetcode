new = ''
s = "A man, a plan, a canal: Panama"

for c in s:
    if c.isalnum():
        new += c.lower()
        
print(new == new[::-1])