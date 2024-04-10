from collections import deque


deck = [17,13,11,2,3,5,7]

q = deque(range(len(deck)))
deck.sort()
ans = [0] * len(deck)

for card in deck:
    index = q.popleft()
    ans[index] = card
    if q:
        q.append(q.popleft())

print(ans)
