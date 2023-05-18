import collections

s = "anagram"
t = "nagaram"

print(collections.Counter(s) == collections.Counter(t))
