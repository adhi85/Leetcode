from collections import defaultdict
strs = ["eat","tea","tan","ate","nat","bat"]

dic = defaultdict(list)

for w in strs:
    dic["".join(sorted(w))].append(w)

print(dic.values())